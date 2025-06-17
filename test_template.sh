#!/bin/sh
# Simple script to test the template locally
set -x -e

PROJ_DIR='python-hatch-project'

cd ..
if [ -d "$PROJ_DIR" ]; then
  rm -rf "$PROJ_DIR"
fi

cookiecutter --no-input hatchlor

cd $PROJ_DIR

hatch env prune

hatch build
hatch clean
hatch version

hatch run cov
hatch run lint
hatch run typecheck
hatch run docs:build

hatch run pre-commit run --all-files
