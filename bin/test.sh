#!/bin/bash

BASEDIR="$(dirname "$0")"
ROOT="$(realpath $BASEDIR/..)"
PYTH="$(which python)"
PWD="$(pwd)"

cd $ROOT

$PYTH $ROOT/test/test.py

cd $PWD