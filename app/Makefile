PROJECT_FOLDER = 'app'
image ?= 'maja-app'
git_hash ?= $(shell git rev-parse --short HEAD)

help: ## print this message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| sort \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "%-30s %s\n", $$1, $$2}'

format: ## format code (with black & isort)
	poetry run black .
	poetry run isort .

.PHONY: init
init: config_gemfury ## Install packages (with poetry)
	poetry install

.PHONY: test
test:  ## Run pytest
	poetry run pytest -vv tests \
		--cov=${PROJECT_FOLDER} \
		--cov-config=.coveragerc

.PHONY: docker-build
docker-build: ## Build Docker image
	poetry export -f requirements.txt > requirements.txt
	docker build -t ${image} --progress=plain .
