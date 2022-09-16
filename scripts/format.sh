#!/bin/sh -e
set -x

autoflake --ignore-init-module-imports --remove-all-unused-imports --recursive --remove-unused-variables --in-place app common --exclude='*pb*'
black app common
isort app common
