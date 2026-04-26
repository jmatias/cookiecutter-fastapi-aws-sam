# Cookiecutter FastAPI AWS SAM

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for a FastAPI project deployable to AWS Lambda via SAM.

* GitHub repo: https://github.com/jmatias/cookiecutter-fastapi-aws-sam
* Free software: MIT license

## Features

* **FastAPI** with automatic OpenAPI/Swagger documentation
* **AWS Lambda** deployment via SAM with Mangum adapter
* **Dual-mode handler**: API Gateway requests and EventBridge events
* **LocalStack** support for local development and testing
* **Runtime selection**: Python 3.12, 3.13, or 3.14
* Testing setup with pytest (unit, integration, aat markers)
* GitHub Actions CI for Python 3.11, 3.12, and 3.13
* Typer CLI included
* CORS middleware configured

## Quickstart

Install the latest Cookiecutter if you haven't installed it yet:

```bash
pip install -U cookiecutter
```

Generate a Python package project:

```bash
cookiecutter https://github.com/jmatias/cookiecutter-fastapi-aws-sam
```

You'll be prompted for:
- `full_name`: Your name
- `email`: Your email
- `github_username`: Your GitHub username
- `pypi_package_name`: Package name (e.g., `my-api`)
- `runtime`: Lambda Python runtime (python3.12, python3.13, python3.14)
- `project_name`: Human-readable name
- `project_short_description`: One-line description

## Generated Project Structure

```
my-api/
├── src/my_api/
│   ├── main.py              # FastAPI app + Lambda handler
│   ├── config.py            # Environment detection
│   ├── controllers/         # API routers
│   └── ...
├── tests/
├── infra/
│   ├── template.yaml        # SAM template
│   └── samconfig.toml       # SAM config
├── justfile                 # Build commands
└── pyproject.toml
```

## Using the Generated Project

### Local Development

```bash
cd my-api
uv sync                      # Install dependencies
uvicorn my_api.main:app --reload  # Run locally
```

### Deploy to LocalStack

```bash
just build                   # Build with SAM
just deploy-localstack       # Deploy to LocalStack
```

### Run Tests

```bash
pytest                       # Run all tests
pytest -m unit               # Run unit tests only
```
