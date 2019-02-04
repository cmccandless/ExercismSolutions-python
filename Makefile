PYTHON=python

.PHONY: init lint test

init:
	@python -m pip install flake8


lint: FILES := .
lint:
	@$(PYTHON) -m flake8 $(FILES) --exclude '*venv*'

test:
	@$(PYTHON) -m pytest $(OPTS) $(FILES)
