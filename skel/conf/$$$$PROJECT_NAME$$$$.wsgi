import os, sys, site

site.addsitedir('/home/$$$$PROJECT_NAME$$$$/virtualenvs/$$$$PROJECT_NAME$$$$/lib/python2.5/site-packages')

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(BASE_DIR,"apps"))
sys.path.insert(0, os.path.join(BASE_DIR,"lib"))
sys.path.insert(0, PROJECT_ROOT)

sys.stdout = sys.stderr

os.environ['FLAVOR'] = 'dev'

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()