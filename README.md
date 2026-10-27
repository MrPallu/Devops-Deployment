# DevOps Deployment Project

A containerized web application built using Python Flask, Docker, Docker Compose, and Nginx. This project demonstrates the fundamentals of application containerization, reverse proxy configuration, multi-container deployment, and container health monitoring.

## Project Overview

The objective of this project is to deploy a Flask web application using Docker and expose it through an Nginx reverse proxy.

Instead of running the Flask application directly on the host machine, the application runs inside a Docker container. Nginx handles incoming HTTP requests and forwards them to the Flask application.

Docker Compose manages both services together.

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
             Flask Application
```

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| Flask | Backend web framework |
| Docker | Application containerization |
| Docker Compose | Multi-container management |
| Nginx | Reverse proxy |
| Ubuntu WSL2 | Linux development environment |
| Git & GitHub | Version control and code hosting |

## Project Structure

```text
devops-deployment/
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
- Docker image creation using a custom Dockerfile.
- Containerized Flask application.
- Nginx reverse proxy configuration.
- Multi-container deployment using Docker Compose.
- Custom application health endpoint.
- Docker HEALTHCHECK instruction.
- Container status and log inspection.
- Reduced Docker build context using `.dockerignore`.

## Application Endpoints

| Endpoint | Description |
|---|---|
| `/` | Displays the application welcome message |
| `/health` | Returns application health status |

### Health Check Response

```json
{
  "status": "healthy"
}
```

HTTP response status: `200 OK`

## Prerequisites

Make sure the following tools are installed:

- Docker Desktop
- Docker Compose
- WSL2 with Ubuntu
- Git

## Installation and Deployment

### 1. Clone the Repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd devops-deployment
```

### 2. Build and Start Containers

```bash
docker compose up -d --build
```

This command builds the Flask Docker image and starts the Flask and Nginx services in the background.

### 3. Verify Running Containers

```bash
docker compose ps
```

### 4. Access the Application

Open the following URL in your browser:

```text
http://localhost
```

### 5. Test the Health Endpoint

```text
http://localhost/health
```

Expected response:

```json
{"status": "healthy"}
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

## Useful Docker Commands

| Command | Purpose |
|---|---|
| `docker compose up -d --build` | Build and start services |
| `docker compose ps` | View service status |
| `docker compose logs` | View service logs |
| `docker compose logs nginx` | View Nginx logs |
| `docker compose logs flask` | View Flask logs |
| `docker compose down` | Stop and remove containers and network |
| `docker images` | List Docker images |
| `docker ps -a` | List all containers |

## Nginx Reverse Proxy

Nginx listens on port 80 and forwards incoming requests to the Flask service on port 5000.

The Flask container is accessible to Nginx through the Docker Compose network. Users access the application through Nginx rather than connecting directly to Flask.

## Learning Outcomes

Through this project, I gained practical experience with:

1. Linux environment setup using WSL2.
2. Python Flask application development.
3. Dockerfile creation and image building.
4. Docker container lifecycle management.
5. Port mapping and container networking.
6. Nginx reverse proxy configuration.
7. Multi-container deployment with Docker Compose.
8. Application health checks and Docker monitoring.
9. Git-based project management.

## Future Improvements

- Implement GitHub Actions for Continuous Integration.
- Automate Docker image builds.
- Push Docker images to Docker Hub.
- Deploy the application on AWS EC2.
- Add Prometheus and Grafana for monitoring.
- Implement automated deployment workflows.

## Author

**Palash Malviya**

B.Tech – Computer Science and Engineering

GitHub: [MrPallu](https://github.com/MrPallu)

---


