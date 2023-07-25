# Run python fastapi app

## build

```
docker build -t fastapi_app .
````

* `docker build`: This is the command to build a Docker image.
* `-t fastapi_app`: This specifies the name of the image (fastapi_app in this case) and tags it with that name.
* `.`: This indicates the build context, which means Docker will look in the current directory and its subdirectories for the Dockerfile and other files needed to build the image.

## run

```
docker run -d -p 8000:8000 fastapi_app
```

* `docker run`: This is the command to run a Docker container.
* `-d`: This flag tells Docker to start the container in detached mode.
* `-p 8000:8000`: This option maps port 8000 from the host to port 8000 in the container. It allows you to access the FastAPI application running in the container via port 8000 on your host machine.
* `fastapi_app`: This is the name of the Docker image you want to run.

## inside container

```bash
# ls
app  bin  boot  dev  etc  home  lib  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
# cd app
# ls
Dockerfile  __pycache__  main.py  requirements.txt
```
there is a VM, you can take a container as a VM.

inside the VM, you got everything you need for a machine. And the most important part `app`, the app we built


`entrypoint and command:`

```
lock-requirements:
  <<: *finance-bank-transaction-ingestion
  entrypoint: /bin/bash
  command: docker/lock_requirements.sh
```


## volumn, bind mount

bind mount, no volume
```
docker run -d -p 8000:8000 -v $(pwd)/data:/app/data fastapi_app
```
Named Volume Mount
```
docker run -d -p 8000:8000 -v data:/app/data fastapi_app
```
`data` is a volume


`TMPFS` (temporary file system) is a type of mount in Docker that allows you to use RAM within a container. It is particularly useful when you need to store temporary or cache data that doesn't need to be persisted between container runs or across multiple containers.

```
docker run -d -p 8000:8000 --tmpfs /app/temp_data fastapi_app
```