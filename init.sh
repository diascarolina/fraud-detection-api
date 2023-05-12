#!/usr/bin/env bash

set -e

exec gunicorn -c gunicorn.py app.app:app

