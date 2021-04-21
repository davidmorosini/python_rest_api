#!/bin/sh

pip install -r requirements.txt
pip install -e .

find . | grep -E "(\.cache|__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

