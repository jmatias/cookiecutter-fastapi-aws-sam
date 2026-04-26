# Show available commands
list:
    @just --list

# Generate project using defaults
bake BAKE_OPTIONS="--no-input":
    cookiecutter {{BAKE_OPTIONS}} . --overwrite-if-exists

# Watch for changes
watch BAKE_OPTIONS="--no-input": bake
    watchmedo shell-command \
        -p '*.*' \
        -c 'just bake {{BAKE_OPTIONS}}' \
        -W -R -D {{'{{cookiecutter.project_slug}}'}}

# Show available commands
help:
    just --list

# Build the project, useful for checking that packaging is correct
build:
    rm -rf build
    rm -rf dist
    poetry build

VERSION := `grep -m1 '^version' pyproject.toml | sed -E 's/version = "(.*)"/\1/'`

# Print the current version of the project
version:
    @echo "Current version is {{VERSION}}"

# Tag the current version in git and put to github
tag:
    echo "Tagging version v{{VERSION}}"
    git tag -a v{{VERSION}} -m "Creating version v{{VERSION}}"
    git push origin v{{VERSION}}

# Run all the tests, but allow for arguments to be passed
test *ARGS:
    @echo "Running with arg: {{ARGS}}"
    poetry run pytest {{ARGS}}

# Run all the tests, but on failure, drop into the debugger
pdb *ARGS:
    @echo "Running with arg: {{ARGS}}"
    poetry run pytest --pdb --maxfail=10 --pdbcls=IPython.terminal.debugger:TerminalPdb {{ARGS}}

# Run all the formatting, linting, type checking, and testing commands
qa:
    poetry run ruff format .
    poetry run ruff check . --fix
    poetry run ruff check --select I --fix .
    poetry run mypy .
    poetry run pytest .

# Run all the checks for CI
ci:
    poetry run ruff format --check .
    poetry run ruff check .
    poetry run ruff check --select I .
    poetry run mypy .
    poetry run pytest .

# Run all the tests for all the supported Python versions
testall:
    tox

# Run coverage, and build to HTML
coverage:
    poetry run coverage run -m pytest .
    poetry run coverage report -m
    poetry run coverage html

# Serve docs locally
doc:
    poetry run mkdocs serve -a localhost:3000

# Build and deploy docs
doc-build:
    poetry run mkdocs gh-deploy --force
