#!/bin/bash
set -ue

apk add --update make

if [ -f requirements.txt ]; then
    make init
fi

make -j8 OPTS='-v' lint test
