#!/bin/bash

IFS="`printf "\n\t"`"
set -e
cd "`dirname "$0"`"

./_bootstrap.sh

cd ..

PROJ_PATH="`pwd`"
PROJ_NAME="`basename "$PROJ_PATH"`"

[[ ! -d "env/" ]] && mkdir env
virtualenv --no-site-packages env/$PROJ_NAME

[[ "$WORKON_HOME" == "" ]] && exit

ln -s "`pwd`/env/$PROJ_NAME" "$WORKON_HOME/$PROJ_NAME"
