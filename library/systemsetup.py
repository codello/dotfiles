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
module: systemsetup

author:
- Kim Wittenburg (@codello)

short_description: Manage system properties via the systemsetup tool.

description:
- systemsetup allows users to configure macOS systems using the systemsetup
  tool. 
- Supports any command that is supported by systemsetup.

options:
  setting:
    description:
      - The name of the setting to modify. This corresponds to the systemsetup
        flag without the -set prefix.
      - Only settings that have a corresponding -get flag are supported.
      - The key may contain underscores (computer_name and computername are
        treated equally).
    type: str
    required: true
  value:
    description:
      - The value for the setting.
      - Boolean values are automatically converted to the strings 'on' and
        'off'.
    type: raw
    required: true
  path:
    description:
      - A colon-separated path where to look for the systemsetup binary.
    required: false
    type: str
'''

EXAMPLES = '''
# Set the computer name
- systemsetup:
    setting: computername
    value: My MacBook

# Disable remote apple events
# Instead of C(off) you could also write C("off"), C(false), etc.
- systemsetup:
    setting: remoteappleevents
    value: off

# Set the display sleep delay to 5 minutes
- systemsetup:
    setting: displaysleep
    value: 5
'''


class SystemSetupException(Exception):
    """An exception raised when working with the systemstup tool."""

    def __init__(self, message):
        self.message = message


class SystemSetup(object):
    def __init__(self, module):
        self.module = module
        self.setting = module.params['setting']
        self.value = module.params['value']
        self.path = module.params['path']

        self.executable = self.module.get_bin_path(
            'systemsetup',
            required=False,
            opt_dirs=self.path.split(':')
        )
        if not self.executable:
            raise SystemSetupException(
                "Unable to locate systemsetup executable."
            )

        self.setting = self.setting.replace("_", "")
        if isinstance(self.value, bool):
            self.value = "on" if self.value else "off"

    def run(self):
        try:
            old = self.run_with_arguments('-get' + self.setting)
        except SystemSetupException:
            raise SystemSetupException(
                message="Invalid setting: " + self.setting
            )
        self.run_with_arguments('-f', '-set' + self.setting, self.value)
        new = self.run_with_arguments('-get' + self.setting)
        return old != new

    def run_with_arguments(self, *args):
        rc, out, err = self.module.run_command([self.executable, *args])
        if rc != 0:
            # It seems that the systemsetup program does not make use of the
            # stderr.
            raise SystemSetupException(message=out)
        if out.startswith("Error:"):
            raise SystemSetupException(message=out)
        return out


def main():
    """Runs the module."""
    module = AnsibleModule(
        argument_spec={
            "setting": dict(type='str', required=True),
            "value": dict(type='raw', required=True),
            "path": dict(type='str', default='/usr/sbin')
        },
        supports_check_mode=False,
    )

    try:
        system_setup = SystemSetup(module=module)
        module.exit_json(changed=system_setup.run())
    except SystemSetupException as error:
        module.fail_json(msg=error.message)


if __name__ == '__main__':
    main()
