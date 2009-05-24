#!/usr/bin/env bash

curl http://peak.telecommunity.com/dist/ez_setup.py > /tmp/ez_setup.py
sudo python /tmp/ez_setup.py -U setuptools

sudo easy_install python-packages/virtualenv-1.3.3.tar.gz
sudo easy_install python-packages/virtualenvwrapper-1.15.tar.gz

PYTHON_BASE=$(dirname `which python`)

touch ~/.profile
mkdir ~/.virtualenvs

if [ ! "$(grep WORKON_HOME ~/.profile)"  ]
    then echo "
export WORKON_HOME=\$HOME/.virtualenvs
source $PYTHON_BASE/virtualenvwrapper_bashrc
" >> ~/.profile
fi

source ~/.profile