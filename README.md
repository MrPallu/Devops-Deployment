# DevOps Deployment Project

A production-oriented containerized web application built using Python Flask, Gunicorn, Docker, Docker Compose, and Nginx. This project demonstrates containerization, reverse proxy configuration, CI/CD automation, container security, health monitoring, and cloud deployment.

## Project Overview

The objective of this project is to deploy a Flask web application using Docker and expose it through an Nginx reverse proxy.

The application runs inside a Docker container using Gunicorn as its WSGI server. Nginx handles incoming HTTP requests and forwards them to Flask. Docker Compose manages the multi-container environment.

The project also implements a CI/CD pipeline using GitHub Actions to build, test, and publish Docker images to Docker Hub. The application is deployed on Render.

## Architecture

```text
              User / Browser
                    |
                    | HTTP Request
                    v
              Nginx Container
                  Port 80
                    |
                    | Reverse Proxy
                    v
              Flask Container
                  Port 5000
                    |
                    v
             Gunicorn WSGI Server
                    |
                    v
              Flask Application
                    |
                    v
              Health Endpoint
```

### CI/CD Architecture

```text
Developer
    |
    | Git Push
    v
GitHub Repository
    |
    v
GitHub Actions
    |
    | Build Docker Image
    | Run Container Tests
    | Test Health Endpoint
    v
Docker Hub
    |
    v
Published Docker Image

GitHub Repository
    |
    v
Render Auto Deployment
    |
    v
Live Application
```

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| Flask | Backend web framework |
| Gunicorn | Production WSGI server |
| Docker | Application containerization |
| Docker Compose | Multi-container management |
| Nginx | Reverse proxy |
| Git & GitHub | Version control |
| GitHub Actions | CI/CD automation |
| Docker Hub | Docker image registry |
| Render | Cloud deployment |
| Ubuntu WSL2 | Linux development environment |

## Project Structure

```text
devops-deployment/
│
├── .github/
│   └── workflows/
│       └── docker-build.yml
│
├── app/
│   ├── app.py
│   └── requirements.txt
│
├── nginx/
│   └── nginx.conf
│
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
└── README.md
```

## Features

- Flask-based web application.
- Production server using Gunicorn.
- Custom Dockerfile for image creation.
- Nginx reverse proxy configuration.
- Multi-container deployment using Docker Compose.
- Application health endpoint.
- Docker HEALTHCHECK instruction.
- Non-root container execution using `appuser`.
- Linux capabilities dropped using `cap_drop: ALL`.
- Container monitoring and log inspection.
- Automated Docker image build and testing through GitHub Actions.
- Docker image publishing to Docker Hub.
- Cloud deployment on Render.

## Application Endpoints

| Endpoint | Description |
|---|---|
| `/` | Displays application welcome message |
| `/health` | Returns application health status |

### Health Check Response

```json
{
  "status": "healthy"
}
```

HTTP response: `200 OK`

## Prerequisites

- Docker Desktop
- Docker Compose
- WSL2 with Ubuntu
- Git
- GitHub account

## Installation and Deployment

### 1. Clone the Repository

```bash
git clone https://github.com/MrPallu/Devops-Deployment.git
cd Devops-Deployment
```

### 2. Build and Start Containers

```bash
docker compose up -d --build
```

### 3. Verify Running Containers

```bash
docker compose ps
```

### 4. Access the Application

Open:

```text
http://localhost
```

### 5. Test the Health Endpoint

```bash
curl http://localhost/health
```

Expected response:

```json
{"status":"healthy"}
```

## Docker Health Monitoring

The Dockerfile includes a HEALTHCHECK instruction that periodically checks whether the Flask application is responding.

Health check configuration:

- Interval: 30 seconds
- Timeout: 3 seconds
- Start period: 5 seconds
- Retries: 3

Check container health:

```bash
docker inspect --format='{{.State.Health.Status}}' flask-container
```

Expected output:

```text
healthy
```

## Container Security

The Flask container includes basic security hardening measures.

### 1. Non-root User

The application runs using a dedicated Linux user named `appuser` instead of the root user.

### 2. Linux Capability Restriction

The Docker Compose configuration uses:

```yaml
cap_drop:
  - ALL
```

This removes Linux capabilities from the Flask container to reduce unnecessary privileges.

### 3. Read-only Nginx Configuration

The Nginx configuration is mounted as read-only:

```yaml
- ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro
```

## CI/CD Pipeline

GitHub Actions automates the Docker image build and testing process.

Pipeline steps:

1. Checkout source code.
2. Build Docker image.
3. Run a temporary Docker container.
4. Test the application health endpoint.
5. Stop the test container.
6. Push the Docker image to Docker Hub.

Docker Hub image:

`palash6700/devops-flask-app:latest`

The pipeline uses GitHub Secrets for Docker Hub authentication.

## Cloud Deployment

The application is deployed on Render.

**Live Application:**

https://devops-deployment-bc5v.onrender.com

Health endpoint:

https://devops-deployment-bc5v.onrender.com/health

The Render deployment is connected to the GitHub repository for automatic deployment when changes are pushed.

## Useful Docker Commands

| Command | Purpose |
|---|---|
| `docker compose up -d --build` | Build and start services |
| `docker compose ps` | View service status |
| `docker compose logs` | View service logs |
| `docker compose logs flask` | View Flask logs |
| `docker compose logs nginx` | View Nginx logs |
| `docker compose down` | Stop and remove containers |
| `docker images` | List Docker images |
| `docker ps -a` | List all containers |

## Learning Outcomes

Through this project, I gained practical experience with:

1. Linux environment setup using WSL2.
2. Flask application development.
3. Dockerfile creation and image building.
4. Container lifecycle management.
5. Container networking and port mapping.
6. Nginx reverse proxy configuration.
7. Multi-container deployment using Docker Compose.
8. Gunicorn and WSGI fundamentals.
9. Container health checks and monitoring.
10. Docker container security.
11. Git-based project management.
12. CI/CD automation using GitHub Actions.
13. Docker image publishing using Docker Hub.
14. Cloud application deployment using Render.

## Future Improvements

- Infrastructure deployment using AWS.
- Infrastructure as Code using Terraform.
- Monitoring with Prometheus and Grafana.
- Centralized logging.
- Kubernetes orchestration.
- Advanced automated deployment strategies.

## Author

**Palash Malviya**

B.Tech – Computer Science and Engineering

GitHub: https://github.com/MrPallu

Project Repository: https://github.com/MrPallu/Devops-Deployment
