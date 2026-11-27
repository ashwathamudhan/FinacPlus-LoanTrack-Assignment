# LoanTrack – Three-Tier Loan Management Application

A DevOps/SRE technical assignment demonstrating application development, containerization, database reliability, Kubernetes deployment and automation.

## Technology Stack

- Frontend: HTML, CSS, JavaScript and Nginx
- Backend: Python Flask
- Database: PostgreSQL
- Containerization: Docker and Docker Compose
- Orchestration: Kubernetes with Minikube
- Automation: Bash

## Project Status

Development in progress.

## Documentation

- BRANCHING.md – Git branching strategy
- EVIDENCE.md – Verification and testing evidence
- AI_USAGE.md – AI assistance disclosure

## Security

Secrets and environment-specific credentials must not be committed to the repository.

## Setup Instructions

To be added as the application is implemented and verified.

## Docker Containerization

LoanTrack consists of three independently containerized application tiers.

| Component | Technology   | Container Port |
| --------- | ------------ | -------------- |
| Frontend  | Nginx        | 80             |
| Backend   | Python Flask | 5000           |
| Database  | PostgreSQL   | 5432           |

### Build Docker Images

Run the following commands from the project root:

```bash
docker build -t loantrack-backend:1.0.0 ./backend
docker build -t loantrack-frontend:1.0.0 ./frontend
docker build -t loantrack-db:1.0.0 ./db
```

### Verify Images

```bash
docker images --filter "reference=loantrack-*"
```

### Container Configuration

- Multi-stage backend Docker build.
- Non-root backend application user.
- Version-tagged base images.
- Separate health checks for each application tier.
- Nginx reverse proxy for backend API requests.
- PostgreSQL migration and seed initialization.
- Docker build context exclusions using .dockerignore.

Docker Compose will be used to configure service networking, environment variables and persistent database storage.
