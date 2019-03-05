#!/bin/bash
set -ue

if [ -f requirements.txt ]; then
    make init
fi

make -j8 OPTS='-v' lint test
