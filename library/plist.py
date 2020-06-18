#!/usr/bin/env python3

import os

from ansible.module_utils.basic import AnsibleModule

ANSIBLE_METADATA = {
    'metadata_version': '0.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: plist

author:
- Kim Wittenburg (@codello)

short_description: Manage Apple Property Lists

description:
- plist allows users to read, write and delete values in Apple property
  lists (plists).
- Currently entries at arbitrary paths can be set or deleted.

options:
  dest:
    description:
      - The absolute path to the plist file to manage (including the file
        extension).
      - A relative path will be interpreted relative to the user's preference
        directory (~/Library/Preferences) and must not include the file
        extension.
    type: str
    required: true
  key:
    description:
      - A dot-separated key path to the value to be modified.
    type: str
    required: true
  state:
    description:
      - The state of the key in dest.
    required: false
    type: str
    choices: [ present, absent ]
    default: present
  value:
    description:
      - The value to write to dest.
      - Only required when C(state=present). 
    type: raw
'''

EXAMPLES = '''
# Set a key in an dictionary
- plist:
    dest: /some/file.plist
    key: Path.To.Key
    value: Some Value 

# Set a preference in a user preference file
- plist:
    dest: com.apple.finder
    key: DesktopViewSettings.IconViewSettings.arrangeBy
    value: grid
'''


class PlistException(Exception):
    """An exception raised when working with plists."""

    def __init__(self, message):
        self.message = message


class Plist(object):
    def __init__(self, module):
        self.module = module
        self.dest = module.params['dest']
        self.state = module.params['state']
        self.key = module.params['key']
        self.value = module.params['value']

    def run(self):
        try:
            import plistlib
        except ImportError:
            raise PlistException(
                message="plistlib is required for the plist module."
            )

        with open(self.dest, 'rb') as file:
            data = plistlib.readPlist(file)
        changed = self.process_data(data)
        if changed and not self.module.check_mode:
            with open(self.dest, 'wb') as file:
                plistlib.writePlist(data, file)
        return changed

    def process_data(self, data):
        """
        Processes plist data according to the module parameters. The `data`
        parameter is mutated accordingly and `True` is returned iff the data has
        been mutated.

        :param data: A dictionary of data to be processed.
        :return: A boolean value indicating whether the `data` argument has been
                 mutated.
        """
        working_data, key = self.get_working_data(data)

        if self.state == 'absent':
            if key not in working_data:
                return False
            del working_data[key]
            return True

        if self.state == 'present':
            if key in working_data and self.value == working_data[key]:
                return False
            working_data[key] = self.value
            return True

        raise PlistException(message="Invalid state: " + self.state)

    def get_working_data(self, data):
        """
        Parses a dot-separated path of keys into a dictionary and returns the
        target dictionary and. Consider for example the path Some.Key.Path. Then
        `get_working_date({"Some": {"Key": {"Path": "Value"}}})` returns
        {"Path": "Value"} and the key "Path".

        For embedded arrays the function supports parsing numeric arguments.

        :param data: A dataset.
        :return: A tuple of data and a key that can access the targeted data in
                 `data`.
        """
        key_path = self.key.split('.')
        for key in key_path[:-1]:
            if isinstance(data, list):
                key = int(key)
            data = data[key]
        key = key_path[-1]
        if isinstance(data, list):
            key = int(key)
        return data, key


def main():
    """Runs the module."""
    module = AnsibleModule(
        argument_spec={
            "dest": dict(type='str', required=True),
            "state": dict(type='str', required=False, default='present',
                          choices=['present', 'absent']),
            "key": dict(type='str', required=True),
            "value": dict(type='raw')
        },
        supports_check_mode=True,
        required_if=(
            ('state', 'present', ['value']),
        )
    )

    if not module.params['dest'].startswith("/"):
        module.params['dest'] = os.path.expanduser(
            "~/Library/Preferences/%s.plist" % module.params['dest'])

    try:
        plist = Plist(module=module)
        module.exit_json(changed=plist.run())
    except PlistException as error:
        module.fail_json(msg=error.message)


if __name__ == '__main__':
    main()
