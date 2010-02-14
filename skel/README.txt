GETTING SET UP
--------------

After checking out the project, run './setup/setup.sh'

This will use 'sudo' to install 'easy_install' (if it isn't already
installed), then 'sudo easy_install virtualenv' and 'sudo easy_install
virtualenvwrapper' if they aren't already installed.

Next, it will create a virtual environment in 'env/' and install Django and
the other requirements listed in setup/requirements.txt.

HACKING
-------

Once the setup has finished, use 'workon $$$$PROJECT_NAME$$$$' to activate the
virtual environment.

Use './bin/run' to run a development server and './bin/run reset' to reset the
working environment (remove and recreate the database, etc).
