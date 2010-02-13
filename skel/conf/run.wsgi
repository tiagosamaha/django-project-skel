import os, sys, site

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(PROJECT_ROOT,"apps"))
sys.path.insert(0, os.path.join(PROJECT_ROOT,"lib"))
sys.path.insert(0, PROJECT_ROOT)

site.addsitedir(os.path.join(PROJECT_ROOT, "env"))

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import django.core.handlers.wsgi

sys.stdout = sys.stderr
application = django.core.handlers.wsgi.WSGIHandler()
