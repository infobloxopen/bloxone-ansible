DIRS="plugins" "tests/integration" "tests/unit"

.PHONY: black
black:
	black -v $(DIRS)

.PHONY: black-lint
black-lint:
	black --check --diff $(DIRS)

.PHONY: flynt
flynt:
	flynt $(DIRS)

.PHONY: flynt-lint
flynt-lint:
	flynt --dry-run --fail-on-change $(DIRS)

.PHONY: isort
isort:
	isort $(DIRS)

.PHONY: isort-lint
isort-lint:
	isort --check-only --diff $(DIRS)

fmt:
	@echo "Running flynt, isort and black"
	@make flynt
	@make isort
	@make black

.PHONY: lint
lint:
	@echo "Running flynt-lint, isort-lint and black-lint"
	@make flynt-lint
	@make isort-lint
	@make black-lint
