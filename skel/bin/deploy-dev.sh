#!/usr/bin/env bash

ssh -t $$$$PROJECT_NAME$$$$@$$$$DEV_APP_HOST$$$$ "\
cd /home/$$$$PROJECT_NAME$$$$/$$$$PROJECT_NAME$$$$/;\
git pull; sudo /etc/init.d/memcached stop;\
sudo /etc/init.d/memcached start;\
sleep 2;\
sudo /etc/init.d/apache2 reload;\
"