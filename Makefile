.PHONY: install
install:
	poetry install --no-root --with=main

.PHONY: install-dev
install-dev: install
	poetry install --no-root --with=dev

.PHONY: install-test
install-test:
	poetry config virtualenvs.in-project true
	poetry install --no-root --with=dev

.PHONY: test
test: install-dev
	poetry run python manage.py test --settings={{project_name}}.settings.test

.PHONY: build-tests
build-tests:
	docker build -f compose/test/Dockerfile -t {{project_name}}_test .

.PHONY: build-run-test
build-run-test:
	make build-tests
	make test