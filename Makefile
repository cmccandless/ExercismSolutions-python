ifeq ($(PYTHON),)
PYTHON:=python
endif
EXTENSION:=py
SOURCE_FILES := $(shell find * -type f -name '*.$(EXTENSION)')
EXERCISES := $(shell find * -type f -name '*.$(EXTENSION)' | cut -d/ -f1 | uniq)
LINT_TARGETS := $(addprefix lint-,$(EXERCISES))
MIGRATE_TARGETS := $(addprefix migrate-,$(EXERCISES))
OUT_DIR=.build
OBJECTS=$(addprefix $(OUT_DIR)/,$(EXERCISES))
LINT_OBJECTS := $(addprefix $(OUT_DIR)/,$(LINT_TARGETS))
MIGRATE_OBJECTS := $(addsuffix /.exercism/metadata.json, $(EXERCISES))
METADATA_FILE:=.exercism/metadata.json

.PHONY: init clean lint test no-skip migrate 
all: lint test
pre-push pre-commit: no-skip migrate lint test
init:
	@python -m pip install -r requirements.txt
lint: $(LINT_TARGETS)
test: $(EXERCISES)
clean:
	rm -rf $(OUT_DIR)

no-skip:
	@ ! (grep -r --exclude-dir='venv*' 'unittest.skip' | grep -v extra-credit)
migrate: $(MIGRATE_TARGETS)

$(LINT_TARGETS) $(EXERCISES): %: $(OUT_DIR)/%
$(MIGRATE_TARGETS): migrate-%: %/$(METADATA_FILE)

$(MIGRATE_OBJECTS):
	@ [ -f $@ ]

$(OUT_DIR):
	@ mkdir -p $@

.SECONDEXPANSION:

GET_DEP = $(filter $(patsubst $(OUT_DIR)/%,%,$@)%,$(SOURCE_FILES))
$(OBJECTS): $$(GET_DEP) | $(OUT_DIR)
	$(eval EXERCISE := $(patsubst $(OUT_DIR)/%,%,$@))
	@ echo "Testing $(EXERCISE)..."
	@ cd $(EXERCISE) && $(PYTHON) -m pytest $(TEST_OPTS)
	@ touch $@

GET_DEP_LINT = $(filter $(patsubst $(OUT_DIR)/lint-%,%,$@)%,$(SOURCE_FILES))
$(LINT_OBJECTS): $$(GET_DEP_LINT) | $(OUT_DIR)
	$(eval EXERCISE := $(patsubst $(OUT_DIR)/lint-%,%,$@))
	@ echo "linting $(EXERCISE)..."
	@ $(PYTHON) -m flake8 $(LINT_OPTS) $(EXERCISE)
	@ touch $@
