import os
import sys

DIR = "/var/www/remo-planet"

os.chdir(DIR)
execfile('env/bin/activate_this.py', dict(__file__='env/bin/activate_this.py'))
sys.path.insert(0, 'rplanet')
os.environ['DJANGO_SETTINGS_MODULE'] = 'rplanet.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
