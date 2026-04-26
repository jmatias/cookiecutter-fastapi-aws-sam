## Project Overview

This is a **Cookiecutter template** for generating FastAPI projects deployable to AWS Lambda via SAM.
The template uses Mangum as the ASGI adapter for AWS Lambda.

**Key distinction**: There are two levels to this project:
1. **Template level** (this repo): The cookiecutter template itself with `{{cookiecutter.*}}` placeholders
2. **Generated project level**: The output when you run `cookiecutter` on this template

## Common Commands

### Template Development (this repo)
```bash
just bake                    # Generate project using defaults (--no-input)
just bake --replay           # Regenerate with previous inputs
just watch                   # Auto-regenerate on template changes
```

### Quality Assurance (this repo)
```bash
just qa                      # Format, lint, type-check, and test
just ci                      # CI checks (format check, lint, type-check, test)
just test                    # Run tests (accepts args: just test -k test_name)
just pdb                     # Tests with IPython debugger on failure
just testall                 # Test across Python 3.10-3.13
just coverage                # Run coverage and build HTML report
```

### Build & Release
```bash
just build                   # Build package (uv build)
just version                 # Show current version
just tag                     # Git tag and push current version
```

### Documentation
```bash
just doc                     # Serve docs locally (localhost:3000)
just doc-build               # Build and deploy docs to GitHub Pages
```

## Architecture

### Template Structure
```
{{cookiecutter.pypi_package_name}}/
├── src/{{cookiecutter.project_slug}}/
│   ├── main.py              # FastAPI app + AWS Lambda handler
│   ├── config.py            # Environment config (AWS_LAMBDA detection, CORS)
│   ├── model.py             # Pydantic models
│   ├── controllers/         # FastAPI routers (fruits, vegetables, activity)
│   ├── cli.py               # Typer CLI app
│   ├── utils.py             # Utility functions
│   └── version_utils.py     # Dynamic version from pyproject.toml
├── tests/
├── infra/
│   ├── template.yaml        # SAM template for Lambda + API Gateway
│   └── samconfig.toml       # SAM deployment config
├── pyproject.toml
├── justfile                 # Generated project commands (build, deploy)
└── Makefile                 # SAM build helper
```

### FastAPI/Lambda Integration Pattern
The generated app uses a dual-mode handler in `main.py`:
- **API Gateway requests**: Routed through Mangum adapter to FastAPI
- **EventBridge events**: Detected via `detail-type`/`detail` keys, handled directly

```python
def handler(event, context):
    if "detail-type" in event and "detail" in event:
        # EventBridge handler
        return {"statusCode": 200, "body": "..."}
    else:
        return Mangum(app, lifespan="on")(event, context)
```

### Generated Project Commands
```bash
just build                   # SAM build with LocalStack
just deploy-localstack       # Deploy to LocalStack
just delete-localstack       # Delete stack from LocalStack
```

### Config Auto-Detection
`config.py` detects Lambda environment via `AWS_LAMBDA` env var and adjusts:
- `FASTAPI_ROOT_PATH`: Set to "/Dev" in Lambda for API Gateway stage prefix
- Swagger servers list includes localhost and SAM local endpoints

## Conventions

- **Python**: 3.12+ (runtime selectable: 3.12, 3.13, 3.14), uv for dependency management
- **Formatting**: ruff (Black-compatible), line-length 100
- **Type hints**: Use `Optional[T]` over `T | None`
- **Testing**: pytest with markers: `unit`, `integration`, `aat`
- **Controllers**: Each resource gets its own router file in `controllers/`, mounted with prefix in `main.py`
- **Models**: Pydantic models with `model_config` for JSON schema examples
- **IaC**: AWS SAM templates in `infra/`, LocalStack for local development

## Cookiecutter Variables

From `cookiecutter.json`:
- `full_name`: Author's full name
- `email`: Author's email
- `github_username`: GitHub username (used for `__gh_slug`)
- `pypi_package_name`: Package name (used for directory names)
- `project_slug`: Python module name (auto-derived: hyphens → underscores)
- `project_name`: Human-readable project name
- `project_short_description`: One-line project description
- `runtime`: Lambda runtime selection (python3.12, python3.13, python3.14)
- `first_version`: Initial version number
