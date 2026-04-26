
clean:
	rm -rf "$(ARTIFACTS_DIR)"

build-FastApiFunction: clean
	poetry lock
	poetry export -f requirements.txt --output src/requirements.txt --without-hashes
	rm -rf "$(ARTIFACTS_DIR)"

	pip install --platform manylinux2014_x86_64 \
		--implementation cp \
		--python-version "{{ cookiecutter.runtime.replace('python', '') }}" \
		--only-binary=:all: \
		--upgrade \
		--target "$(ARTIFACTS_DIR)" \
		-r src/requirements.txt

	cp -vr src/{{cookiecutter.project_slug}} "$(ARTIFACTS_DIR)/"
	cp -vf pyproject.toml "$(ARTIFACTS_DIR)/{{cookiecutter.project_slug}}/pyproject.toml"
