PYTHON=python3.6

.PHONY: lint test
lint: FILES := .
lint:
	@$(PYTHON) -m flake8 $(FILES)

test:
	@$(PYTHON) -m pytest $(OPTS) $(FILES)
