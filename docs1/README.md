# Django Project with Docker

This is a basic Django project setup with Docker support. It includes a `Dockerfile` for containerization and a `requirements.txt` for managing dependencies. This guide will walk you through setting up and running the Django project using Docker.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Build the Docker Image](#2-build-the-docker-image)
  - [3. Run the Docker Container](#3-run-the-docker-container)
  - [4. Apply Migrations](#4-apply-migrations)
  - [5. Access the Application](#5-access-the-application)
- [Development Workflow](#development-workflow)
  - [1. Modify the Code](#1-modify-the-code)
  - [2. Rebuild the Docker Image](#2-rebuild-the-docker-image)
  - [3. Run Tests](#3-run-tests)
- [Dockerfile & Requirements.txt](#dockerfile-requirementstxt)

## Prerequisites

Before starting, ensure you have the following installed:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/) (optional for multi-container apps)
- Python 3.x (for local development without Docker)
- [Git](https://git-scm.com/)


## Installation using Docker

1. Build the Docker image:
   ```sh
   docker build -t onepiece_project .
