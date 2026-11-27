# AI Usage Disclosure

## Tool Used

ChatGPT (OpenAI)

## Purpose

AI assistance is being used to understand DevOps concepts, plan implementation steps, explain commands and configuration, and support troubleshooting and documentation.

## Verification

Commands, configurations and generated suggestions will be reviewed and tested locally before being considered complete.

## Responsibility

The project owner is responsible for understanding the implementation, verifying the results, and ensuring that the submitted evidence reflects actual work.

## Usage Log

### Stage 2 – Git and GitHub

AI assistance used for Git workflow guidance, repository documentation and explanation of version-control concepts.

Additional usage will be documented during later stages.

## Stage 4 – Docker and Containerization

**AI tool used:** ChatGPT

**Purpose of AI assistance:**

- Understanding Docker images, containers and Dockerfiles.
- Preparing a multi-stage Dockerfile for the Flask backend.
- Understanding non-root container execution.
- Preparing Nginx configuration and the frontend Dockerfile.
- Preparing the PostgreSQL Dockerfile and database initialization configuration.
- Understanding Docker health checks and .dockerignore files.
- Troubleshooting container name conflicts and host port binding errors.

**Manual implementation and verification:**

- Created Docker configuration files using VS Code.
- Executed Docker build commands using PowerShell.
- Verified the backend non-root user.
- Diagnosed the frontend port conflict using netstat and Windows port exclusion commands.
- Resolved the port conflict by switching the frontend host port from 8080 to 8081.
- Verified the frontend container health status.
- Built and inspected all three Docker images.

**Learning outcomes:**

Understood Docker build contexts, multi-stage builds, image tagging, container networking, port mapping, health checks, database initialization and basic container security.
