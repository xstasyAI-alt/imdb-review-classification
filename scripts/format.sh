#!/bin/sh -e
set -x

autoflake --ignore-init-module-imports --remove-all-unused-imports --recursive --remove-unused-variables --in-place src --exclude='*pb*'
black src
isort src
