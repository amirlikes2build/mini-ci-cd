# Mini CI/CD FastAPI Pipeline

A small FastAPI project used to learn and demonstrate a complete CI/CD pipeline with tests, Docker, GitHub Actions, GitHub Container Registry, and Render.

## What this project demonstrates

- FastAPI API development
- Unit testing with pytest
- API endpoint testing with FastAPI TestClient
- Linting with Ruff
- Docker image builds
- Docker image tagging with `latest` and the Git commit SHA
- Publishing images to GitHub Container Registry
- Multi-job GitHub Actions workflows
- Deployment to Render using a deploy hook

## Tech stack

- Python
- FastAPI
- Uvicorn
- pytest
- Ruff
- Docker
- GitHub Actions
- GitHub Container Registry
- Render

## API endpoints

### Status

```http
GET /
