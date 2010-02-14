#!/bin/bash

IFS="`printf "\n\t"`"
set -e
cd "`dirname "$0"`"

./_bootstrap.sh

cd ..

PROJ_PATH="`pwd`"
PROJ_NAME="`basename "$PROJ_PATH"`"

# Create a virtualenv at env/$PROJ_NAME
[[ ! -d "env/" ]] && mkdir env
virtualenv --no-site-packages "./env/$PROJ_NAME"

# Start the virtual env
OLD_PWD="`pwd`"
source "env/$PROJ_NAME/bin/activate"
cd "$OLD_PWD"

# Install pip then update the requirements
easy_install pip
pip install -U -r setup/requirements.txt

# Finally, create a link in $WORKON_HOME to this virtualenv
if [[ "$WORKON_HOME" != "" ]]
then
    ln -s "`pwd`/env/$PROJ_NAME" "$WORKON_HOME/$PROJ_NAME" || true
    echo "Ready - run 'workon $PROJ_NAME' to start working."
else
    echo "Ready - run '. env/$PROJ_NAME/bin/activate' to start working."
fi

