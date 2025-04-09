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

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/yourrepo.git
   cd yourrepo


## Installation using Docker

1. Build the Docker image:
   docker build -t onepiece_project .

2. Run the Docker container:
   docker run -p 8000:8000 onepiece_project

3. Apply database migrations:
   python manage.py migrate

4. (Optional) Create a superuser:
   python manage.py createsuperuser

5. Access the application in your browser:
   http://localhost:8000


## Development workflow

1. Modify the Code Make changes to your Django views, models, or templates.

2. Rebuild the Docker Image After changes:
   docker build -t onepiece_project .

3. Run Tests Run tests using:
   docker exec -it <container_id_or_name> python manage.py test


## Dockerfile & Requirements.txt

- Dockerfile: Used to create a Docker image that runs your Django app.

- requirements.txt: Lists all Python dependencies required to run the project.

Make sure both of these files are in the same directory as manage.py.
