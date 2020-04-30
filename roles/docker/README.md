# docker

Configures docker. The configuration includes:

- Using docker without sudo
- Installing `docker-compose` on non-macOS systems

On macOS `docker-compose` is never installed because it is included in Docker for Mac. Docker for Mac needs to be installed separately.

## Configuration

The `docker` role can be configured using the `docker` namespace. Available options and their defaults are:

```yaml
docker:
  # If set to yes the user will be added to the docker group. This allows the
  # execution of docker commands without explicit sudo.
  no_password: yes
  
  # Install the specified version of docker compose. This will make sure that
  # the specified version is installed, potentially replacing any older or newer
  # versions. If set to false docker-compose will not be installed.
  #
  # On macOS this is ignored as docker-composed is installed together with
  # docker desktop.
  compose: "1.25.5"
  
  # Specify which location docker-compose will be installed to. By default
  # docker-compose will be installed into ~/.local/bin unless
  # compose_system_install is true in which case it will be installed to
  # /usr/local/bin.
  #
  # This path must not contain the docker-compose file name.
  compose_path: "{{ omit }}"
  
  # Whether to install docker-compose system wide or only for the current user.
  compose_system_install: no

```

