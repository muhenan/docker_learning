# Docker Compose

## Anchor

In yaml/yml, anchor is a complex data structure or variable.

Anchor:
* has alias using &
* to use anchor, using *

```yaml
# Creating an anchor
my_anchor_name: &my_anchor
  key1: value1
  key2: value2
  # ... more key-value pairs ...

# Referencing the anchor using an alias
some_service:
  key1: *my_anchor
```

## Services

```yaml
  local-secret-distributor:
    image: "wayfair/local-secret-distributor:latest"
    environment:
      DISTRIBUTIONS: "gcp_jenkdocker_batch-dev"
    volumes:
      - "local_secret_gcp_jenkdocker_batch-dev:/wayfair/etc/priv/gcp_jenkdocker_batch-dev"
      - "~/.:/root/hosthomedir"
      - "/var/run/docker.sock:/run/docker.sock"
```
The service will use the image tagged latest from the Docker Hub repository wayfair/local-secret-distributor.

environment:
This section defines environment variables for the service. 

volumes:
This section defines the volumes to be mounted inside the container.

* "local_secret_gcp_jenkdocker_batch-dev:/wayfair/etc/priv/gcp_jenkdocker_batch-dev":
This volume mount syntax references the named volume local_secret_gcp_jenkdocker_batch-dev created earlier. It mounts the volume to the path /wayfair/etc/priv/gcp_jenkdocker_batch-dev inside the local-secret-distributor container. This volume is likely used for sharing secrets or configuration files with the local-secret-distributor service.

* "~/.:/root/hosthomedir":
This volume mount syntax binds the host's home directory (~/.) to the path /root/hosthomedir inside the container. This could be useful for accessing configuration files or other data located in the user's home directory on the host machine.

* "/var/run/docker.sock:/run/docker.sock":
This volume mount syntax binds the Docker socket on the host machine (/var/run/docker.sock) to the path /run/docker.sock inside the container. This allows the local-secret-distributor container to communicate with the Docker daemon running on the host machine. This is commonly used for running Docker commands from within a container.


`build -> dockerfile`
```yml
services:
  finance-bank-transaction-ingestion: &finance-bank-transaction-ingestion
    build: &default_build
      dockerfile: ./docker/finance-bank-transaction-ingestion.dockerfile
      context: .
      args:
        <<: *build_args
    environment: &environment
      PYENV_VERSION: "finance-bank-transaction-ingestion"
    entrypoint: sh docker/files/start-service.sh
    # The "@" indicates that all arguments will be passed to the script called by `entrypoint`
    command: "@"
    volumes:
    - ./:/app
    image: "wayfair/finance-bank-transaction-ingestion"
```

## Volume


In this docker-compose.yml snippet, you are defining several named volumes with different configurations for your Docker Compose services. Let's break down each volume:

* home:
  * This is a named volume named home. Named volumes are managed by Docker and provide persistent storage that survives container restarts. In this case, the configuration for the volume is not specified, so it will use the default driver, which is typically local.

* wayfair-data:
  * This is a named volume named wayfair-data, and it has a specific driver set: local. The local driver means that the volume is created and managed locally on the host machine's file system. It is ideal for scenarios where you want the volume to persist on the host.

* local_secret_gcp_jenkdocker_batch-dev:
  * This is a named volume named local_secret_gcp_jenkdocker_batch-dev, and it has a specific driver set: tmpfs. The tmpfs driver allows you to create a temporary, in-memory file system. This volume will not persist on the host; it will only exist in memory while the container is running. The device configuration specifies that it's a tmpfs type volume.

When you use named volumes in Docker Compose, the volumes are automatically created and managed for you. For the volumes with the default driver, Docker will create the volume as a directory on the host machine's file system under /var/lib/docker/volumes/ or a similar location depending on your Docker installation.

For the volume with the tmpfs driver, it will be a temporary in-memory file system, and the data will be lost when the container using it is stopped or removed.




> docker compose 其实没啥，基本就是在调用各种 dockerfile，调用各种 sh 脚本，别忘了，这里有整整一整个 docker 文件夹存放管理这些文件，脚本。