#!/usr/bin/env bash

ssh -t $$$$PROJECT_NAME$$$$@$$$$PROD_APP_HOST$$$$ "\
cd /home/$$$$PROJECT_NAME$$$$/$$$$PROJECT_NAME$$$$/;\
git pull;
sudo /etc/init.d/apache2 reload;\
source /home/$$$$PROJECT_NAME$$$$/virtualenvs/$$$$PROJECT_NAME$$$$/bin/activate;\
export FLAVOR=prod;\
python manage.py flush_all_memcached;\
"