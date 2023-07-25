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