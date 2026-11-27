# LoanTrack – Evidence Log

This document records genuine verification results and supporting screenshots.

## Stage 1 – Environment Setup

Status: Verification details to be recorded.

## Stage 2 – Git and GitHub

Status: In progress.

Evidence to capture:

- Git repository initialization
- Main and develop branches
- Feature branch
- Pull request and review comment
- Merge history

## Later Stages

Docker, database reliability, Kubernetes operations, automation and troubleshooting evidence will be added as each task is completed.

## Troubleshooting Records

Record actual problems, diagnostic commands, root causes and fixes. Do not fabricate failures or results.

# LoanTrack – Evidence

## Stage 3 – Application Development

### Git Branch

Branch: feature/three-tier-app

### Application Structure

- Frontend: HTML, CSS, JavaScript
- Backend: Python Flask
- Database: PostgreSQL

### Implemented Endpoints

- GET /loans
- POST /loans
- GET /healthz
- GET /readyz

### Verification

- Python syntax check: Pending
- JavaScript syntax check: Pending
- Database initialization: Pending Stage 5
- API integration tests: Pending Stage 5
- Frontend integration test: Pending Stage 5

### Evidence Files

- evidence/stage3-project-structure.png
- evidence/stage3-python-syntax.png

### Issues Encountered

Record actual errors, diagnosis, root cause and fix.
Do not invent troubleshooting incidents.

## Stage 4 – Docker and Containerization

### Docker Environment

- Docker version: 28.4.0
- Docker Engine verification: Successful
- Hello-world container execution: Successful

### Docker Image Build Results

| Component | Image                    | Image ID     | Size    |
| --------- | ------------------------ | ------------ | ------- |
| Backend   | loantrack-backend:1.0.0  | 442345f9e36d | 213 MB  |
| Frontend  | loantrack-frontend:1.0.0 | a6391593abfb | 92.6 MB |
| Database  | loantrack-db:1.0.0       | 39fec74ec9e3 | 420 MB  |

### Backend Containerization

- Implemented a multi-stage Docker build using Python 3.12 slim.
- Configured an isolated Python virtual environment.
- Verified non-root execution using appuser with UID and GID 10001.
- Configured a health check using the /healthz endpoint.
- Added a backend .dockerignore file.

### Frontend Containerization

- Created an Nginx-based frontend image.
- Configured reverse proxy routing from /api/ to the backend service.
- Configured a separate frontend health endpoint.
- Verified that the temporary frontend container was running and healthy.
- Used host port 8081 mapped to container port 80.

### Database Containerization

- Built a custom PostgreSQL 16 Alpine image.
- Configured SQL migration and seed initialization.
- Configured a database health check using pg_isready.
- Stopped and removed the temporary database test container.

### Integration Status

All three Docker images have been successfully built. Full application integration, service networking and persistent database storage will be configured and verified in Stage 5 using Docker Compose.

## Stage 6 - Database and Reliability Testing

### 6.1 Database Initialization

- Migration file:
- Seed file:
- Number of seeded records:

### 6.2 Database Connectivity

Command and output:

```text
Paste actual output
```

### 6.3 Health and Readiness Checks

- /healthz response:
- /readyz response:

### 6.4 Loan Creation Through UI

- Borrower name: Reliability Test User
- Loan amount: 750000
- Property city: Chennai

PostgreSQL verification:

```text
Paste actual SQL output
```

### 6.5 Database Failure Test

Command: docker compose stop db

- Health endpoint response:
- Readiness endpoint response:

### 6.6 Database Recovery Test

Command: docker compose start db

- Database status:
- Readiness response:
- Frontend recovery:

### 6.7 Backend Startup Retry and Backoff

Command: docker compose up -d --no-deps backend

Backend retry and recovery logs:

```text
Paste actual retry and recovery logs
```

### 6.8 Database Persistence Test

Commands:

- docker compose down
- docker compose up -d

Before:

```text
Paste actual SQL output
```

After:

```text
Paste actual SQL output
```

### 6.9 Volume Removal Test

Commands:

- docker compose down -v
- docker compose up -d

Result:

```text
Paste actual SQL output
```

Conclusion:
Describe whether the old records were removed and
the original seed records were recreated.

## Stage 8 - Kubernetes Configuration

### Namespace, ConfigMap and Secret

Commands:

```bash
kubectl get namespace loantrack
kubectl get configmap,secret -n loantrack
```

Output:

Paste actual terminal output here.

### Security

Database credentials are stored in a Kubernetes Secret.
The actual secret.yaml is excluded from Git.
Only secret.example.yaml with dummy values is committed.

### Kubernetes - PostgreSQL Deployment

#### Database Deployment and Pod

```bash
kubectl get deployment,pods -n loantrack
```

Output:
Paste actual output here.

#### Database Service

```bash
kubectl get svc -n loantrack
```

Output:
Paste actual output here.

#### Persistent Storage

```bash
kubectl get pvc -n loantrack
kubectl get pv
```

Output:
Paste actual output here.

#### Database Initialization

Paste relevant initialization logs and SELECT COUNT(\*)
query output here.

#### Design Decision

PostgreSQL uses a single-replica Deployment with a PVC.
The Recreate strategy avoids overlapping database instances
during Deployment updates. Persistent storage allows data
to survive Pod replacement.
