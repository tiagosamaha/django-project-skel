#!/usr/bin/env bash

if [ "$1" == "dev" ]; then
    FLAVOR=$1
elif [ "$1" == "prod" ]; then
    FLAVOR=$1
else 
    echo "Usage: $0 (dev|prod)"
    exit 1
fi

TEMP_FILENAME=/tmp/`uuidgen`.json

ssh $$$$PROJECT_NAME$$$$@$$$$DEV_APP_HOST$$$$ "\
cd /home/$$$$PROJECT_NAME$$$$/$$$$PROJECT_NAME$$$$/;\
source /home/$$$$PROJECT_NAME$$$$/virtualenvs/$$$$PROJECT_NAME$$$$/bin/activate;\
FLAVOR=$FLAVOR ./manage.py dumpdata > $TEMP_FILENAME;\
"

scp $$$$PROJECT_NAME$$$$@$$$$DEV_APP_HOST$$$$:$TEMP_FILENAME $TEMP_FILENAME

rm dev.db
FLAVOR=localdev python manage.py syncdb --noinput
FLAVOR=localdev python manage.py migrate
FLAVOR=localdev python manage.py flush --noinput --verbosity=0
FLAVOR=localdev python manage.py delete_contenttypes
FLAVOR=localdev python manage.py loaddata $TEMP_FILENAME