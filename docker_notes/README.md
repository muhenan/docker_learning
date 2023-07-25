# Docker Components

## Volumes

like a seperated database.

Used to store data outside the container's file systems. -> DB

## Docker Compose

`Dockerfile:`

A Dockerfile is a simple text file used to define the instructions to build a Docker image. It contains a set of commands that specify the base image, copy files into the image, set environment variables, and execute commands during the image building process. The Dockerfile is the blueprint for creating a Docker image that encapsulates the application and its dependencies.

The Docker image becomes a standalone and executable package that contains everything needed to run the application, such as the runtime, libraries, and code.

> dockerfile -> docker compose

`Docker Compose:`

Docker Compose is a separate tool that complements Docker and helps you define and manage multi-container applications. It allows you to define multiple containers, their configurations, networks, volumes, and the relationships between them using a single YAML file called docker-compose.yml.

With Docker Compose, you can define the services, networks, and volumes for your entire application stack in a declarative manner. This enables you to manage complex applications with multiple interconnected containers using a simple and unified configuration file.

`The key benefits of Docker Compose include:`

Ease of Orchestration: Docker Compose enables you to spin up an entire multi-container application stack with a single command. It automatically handles the creation, networking, and volume management for all the containers defined in the Compose file.

Scalability and Reproducibility: Docker Compose allows you to scale the application services up or down easily, depending on your needs. You can reproduce the same application stack on different environments (development, staging, production) using the same Compose file.

Isolation and Management: Each service defined in the Compose file remains isolated and can be managed independently. This allows you to update or replace specific containers while the rest of the application continues to run.

Environment Variables and Overrides: Docker Compose supports environment variables and allows you to override default values, making your application configuration more flexible.

`In summary`, while a Dockerfile is used to create a Docker image representing your application, Docker Compose is used to manage and orchestrate multiple containers and services that constitute your application stack. Together, they provide a powerful toolkit for developing, deploying, and managing complex applications using Docker containers.

Example:


Docker Compose file  `docker-compose.yml`:

```yml
version: '3.8'

services:
  fastapi_app:
    image: fastapi_app
    ports:
      - "8000:8000"
    volumes:
      - data_volume:/app/data

volumes:
  data_volume:
```