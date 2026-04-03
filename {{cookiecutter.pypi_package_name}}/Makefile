
build-FastApiFunction:
	poetry lock
	poetry export -f requirements.txt --output src/requirements.txt --without-hashes

	cd src && pip install --platform manylinux2014_x86_64 \
		--only-binary=:all: --upgrade --target "$(ARTIFACTS_DIR)" -r requirements.txt

	mkdir -p "$(ARTIFACTS_DIR)/{{cookiecutter.project_slug}}"
	cd src && cp -vr **/*.py "$(ARTIFACTS_DIR)/{{cookiecutter.project_slug}}"
	cp -vf pyproject.toml "$(ARTIFACTS_DIR)/{{cookiecutter.project_slug}}/pyproject.toml"
