GETTING SET UP FOR THE FIRST TIME
---------------------------------

1. Bootstrap your environment. This only needs to be done once:

    ./python-packages/_bootstrap.sh


2. Create a virtual environment (it doesn't need to be named $$$$PROJECT_NAME$$$$-env,
   but name it something you'll remember):

    mkvirtualenv $$$$PROJECT_NAME$$$$-env


3. Install the "pip" Python package manager in the new virtual environment:

    easy_install python-packages/pip-0.4.tar.gz


4. Upgrade to the latest version of the packages:

    ./bin/upgrade.sh



WHAT YOU SHOULD DO PERIODICALLY
-------------------------------

1. Switch to the correct virtual environment:

    workon $$$$PROJECT_NAME$$$$-env


2. Upgrade to the latest version of the packages:

    ./bin/upgrade.sh



WHAT YOU SHOULD DO EVERY DAY
----------------------------

1. Upgrade to the latest code:

    git pull


2. Switch to the correct virtual environment:

    workon $$$$PROJECT_NAME$$$$-env


3. Start your local development server:

    python manage.py runserver 0.0.0.0:8000