
build-FastApiFunction:
	poetry export -f requirements.txt --output requirements.txt --without-hashes

	cd src && pip install --platform manylinux2014_x86_64 \
		--only-binary=:all: --upgrade --target "$(ARTIFACTS_DIR)" -r requirements.txt

	mkdir -p "$(ARTIFACTS_DIR)/python_fastapi_aws_sam"
	cd src && cp -vr **/*.py "$(ARTIFACTS_DIR)/python_fastapi_aws_sam"
	cp -vf pyproject.toml "$(ARTIFACTS_DIR)/python_fastapi_aws_sam/pyproject.toml"
