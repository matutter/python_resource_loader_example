#!/bin/bash

BASEDIR="$(dirname "$0")"
ROOT="$(realpath $BASEDIR/..)"
PYTH="$(which python)"
PWD="$(pwd)"

cd $ROOT

./bin/build-install-clean.sh
./bin/test.sh

cd $PWD