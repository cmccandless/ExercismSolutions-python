#!/bin/bash
set -ue

apk add --update make

# If requirements.txt contains anything other than flake8 and pytest, uncomment
# if [ -f requirements.txt ]; then
#     make init
# fi

make -j8 TEST_OPTS='-v' lint test
