PYTHON=python3.7
EXTENSION:=py
SOURCE_FILES := $(shell find * -type f -name '*.$(EXTENSION)')
EXERCISES := $(shell find * -type f -name '*.$(EXTENSION)' | cut -d/ -f1 | uniq)
LINT_TARGETS := $(addprefix lint-,$(EXERCISES))
OUT_DIR=.build
OBJECTS=$(addprefix $(OUT_DIR)/,$(EXERCISES))
LINT_OBJECTS := $(addprefix $(OUT_DIR)/,$(LINT_TARGETS))
MIGRATE_OBJECTS := $(addsuffix /.exercism/metadata.json, $(EXERCISES))

.PHONY: init clean lint test-all no-skip check-migrate 
all: lint test
pre-push pre-commit: no-skip check-migrate lint test
init:
	@python -m pip install flake8 pytest
lint: $(LINT_TARGETS)
test: $(EXERCISES)
clean:
	rm -rf $(OUT_DIR)

no-skip:
	@ ! (grep -r --exclude-dir='venv*' 'unittest.skip' | grep -v extra-credit)
check-migrate: $(MIGRATE_OBJECTS)

$(MIGRATE_OBJECTS):
	@ [ -f $@ ] || $(error "$(shell echo $@ | cut -d/ -f1) has not been migrated")

$(LINT_TARGETS) $(EXERCISES): %: $(OUT_DIR)/%

$(OUT_DIR):
	@ mkdir -p $@

.SECONDEXPANSION:

lint: FILES := .
lint:
	@$(PYTHON) -m flake8 $(FILES) --exclude '*venv*'

test:
	@$(PYTHON) -m pytest $(OPTS) $(FILES)



GET_DEP = $(filter $(patsubst $(OUT_DIR)/%,%,$@)%,$(SOURCE_FILES))
$(OBJECTS): $$(GET_DEP) | $(OUT_DIR)
	$(eval EXERCISE := $(patsubst $(OUT_DIR)/%,%,$@))
	@ echo "Testing $(EXERCISE)..."
	@ cd $(EXERCISE) && $(PYTHON) -m pytest $(OPTS)
	@ touch $@

GET_DEP_LINT = $(filter $(patsubst $(OUT_DIR)/lint-%,%,$@)%,$(SOURCE_FILES))
$(LINT_OBJECTS): $$(GET_DEP_LINT) | $(OUT_DIR)
	$(eval EXERCISE := $(patsubst $(OUT_DIR)/lint-%,%,$@))
	@ echo "linting $(EXERCISE)..."
	@ $(PYTHON) -m flake8 $(OPTS) $(EXERCISE)
	@ touch $@
