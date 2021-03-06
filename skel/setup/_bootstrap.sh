#!/usr/bin/env bash

IFS="`printf "\n\t"`"
cd "`dirname "$0"`"

if [[ "`which easy_install`" == "" ]]
then
    echo "Using sudo to intsall easy_install..."
    curl http://peak.telecommunity.com/dist/ez_setup.py > /tmp/ez_setup.py
    sudo python /tmp/ez_setup.py -U setuptools
fi

[[ "`which virtualenv`" != "" ]] && exit
echo "Using sudo to install virtualenv and virtualenvwrapper (workon)"
sudo easy_install virtualenv
sudo easy_install virtualenvwrapper

PYTHON_BASE=$(dirname `which python`)

touch ~/.profile
mkdir ~/.virtualenvs

if [ ! "$(grep WORKON_HOME ~/.profile)"  ]
    then echo "
export WORKON_HOME=\$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper_bashrc
" >> ~/.profile
fi

source ~/.profile

if [[ -f "$WORKON_HOME/postactive" ]]
then
    echo "Postactivate script already exists - not copying."
    echo "If you'd like, you can copy this in to $WORKON_HOME/postactive"
    echo "by hand:"
    cat ./postactive
else
    cp ./postactive $WORKON_HOME/
fi

echo "Installed."
echo "Your new WORKON_HOME is ~/.virtualenvs"
