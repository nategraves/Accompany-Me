import os
import sys
from os.path import abspath, dirname, join
from site import addsitedir

PROJECT_ROOT = abspath(dirname(__file__))

path = addsitedir(join(PROJECT_ROOT, "libs"), set())
if path:
    sys.path = list(path) + sys.path
sys.path.insert(0, join(PROJECT_ROOT, "apps"))

from django.core.handlers.wsgi import WSGIHandler

os.environ['DJANGO_SETTINGS_MODULE'] = 'accompany.settings_prod'
application = WSGIHandler()
