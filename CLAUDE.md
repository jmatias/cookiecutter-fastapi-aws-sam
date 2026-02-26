# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Cookiecutter template** for generating FastAPI projects deployable to AWS Lambda via SAM. The template uses Mangum as the ASGI adapter for AWS Lambda.

**Key distinction**: There are two levels to this project:
1. **Template level** (this repo): The cookiecutter template itself with `{{cookiecutter.*}}` placeholders
2. **Generated project level**: The output when you run `cookiecutter` on this template

## Common Commands

### Template Development (this repo)
```bash
just bake                    # Generate project using defaults (--no-input)
just bake --replay           # Regenerate with previous inputs
just watch                   # Auto-regenerate on template changes
python run.py                # Alternative: watch with auto-regenerate
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
│   ├── controllers/         # FastAPI routers (one per resource)
│   ├── cli.py               # Typer CLI app
│   └── version_utils.py     # Dynamic version from pyproject.toml
├── tests/
├── pyproject.toml           # poetry-core backend, dependencies
└── justfile                 # Generated project commands
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

### Config Auto-Detection
`config.py` detects Lambda environment via `AWS_LAMBDA_FUNCTION_NAME` env var and adjusts:
- `FASTAPI_ROOT_PATH`: Set to "/Dev" in Lambda for API Gateway stage prefix
- Swagger servers list includes localhost and SAM local endpoints

## Conventions

- **Python**: 3.12+, Black formatting (line-length 100), uv for dependency management
- **Type hints**: Use `Optional[T]` over `T | None`
- **Testing**: pytest with markers: `unit`, `integration`, `aat`
- **Controllers**: Each resource gets its own router file in `controllers/`, mounted with prefix in `main.py`
- **Models**: Pydantic models with `model_config` for JSON schema examples

## Cookiecutter Variables

From `cookiecutter.json`:
- `pypi_package_name`: Package name (used for directory names)
- `project_slug`: Python module name (auto-derived: hyphens → underscores)
- `github_username`: Used for `__gh_slug`