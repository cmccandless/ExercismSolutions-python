#!/bin/bash
set -ue

if [ -f requirements.txt ]; then
    python -m pip install -r requirements.txt
fi

python -m flake8
python -m pytest
