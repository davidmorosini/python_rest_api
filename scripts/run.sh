#!/bin/sh
set -e

. ${DOTENV_PATH}

python3 server.py
