# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

* GitHub: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
* Free software: MIT License

## Features

* FastAPI with automatic OpenAPI/Swagger documentation
* AWS Lambda deployment via SAM with Mangum adapter
* Dual-mode handler: API Gateway requests and EventBridge events
* LocalStack support for local development

## Quick Start

### Local Development

```bash
poetry install                             # Install dependencies
poetry run uvicorn {{ cookiecutter.project_slug }}.main:app --reload  # Run locally
```

Open http://localhost:8000/docs for Swagger UI.

### Deploy to LocalStack

```bash
just build                   # Build with SAM
just deploy-localstack       # Deploy to LocalStack
```

### Run Tests

```bash
pytest                       # Run all tests
pytest -m unit               # Run unit tests only
pytest -m integration        # Run integration tests
```

## Project Structure

```
src/{{ cookiecutter.project_slug }}/
├── main.py              # FastAPI app + Lambda handler
├── config.py            # Environment detection
├── controllers/         # API routers
├── model.py             # Pydantic models
└── cli.py               # Typer CLI
```

## Credits

Created with [cookiecutter-fastapi-aws-sam](https://github.com/jmatias/cookiecutter-fastapi-aws-sam).
