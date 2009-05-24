import os, sys, site

site.addsitedir('/home/$$$$PROJECT_NAME$$$$/virtualenvs/$$$$PROJECT_NAME$$$$/lib/python2.5/site-packages')

sys.stdout = sys.stderr

os.environ['FLAVOR'] = 'dev'

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()