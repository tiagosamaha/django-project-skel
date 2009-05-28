#!/usr/bin/env bash

SERVERS="$$$$DEV_APP_HOST$$$$ $$$$PROD_APP_HOST$$$$"

for host in $SERVERS; do
    ssh $$$$PROJECT_NAME$$$$@$host "\
    source /home/$$$$PROJECT_NAME$$$$/virtualenvs/$$$$PROJECT_NAME$$$$/bin/activate;\
    cd /home/$$$$PROJECT_NAME$$$$/$$$$PROJECT_NAME$$$$;\
    ./bin/upgrade.sh"
done