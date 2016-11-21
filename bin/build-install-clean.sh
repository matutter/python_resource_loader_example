#!/bin/bash

BASEDIR="$(dirname "$0")"
ROOT="$(realpath $BASEDIR/..)"
PYTH="$(which python)"
PWD="$(pwd)"

cd $ROOT

#uninstall
rm ~/.local/lib/python2.7/site-packages/pactest*

#build + install
$PYTH setup.py install --user

#clean
rm -rf $ROOT/build
rm -rf $ROOT/dist
rm -rf $ROOT/*.egg-info

cd $PWD