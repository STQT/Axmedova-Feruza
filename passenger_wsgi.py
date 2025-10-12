import os
import sys

# ЗАМЕНИТЕ username НА ВАШЕ ИМЯ ПОЛЬЗОВАТЕЛЯ
INTERP = os.path.expanduser("~/virtualenv/website/3.12/bin/python")
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

sys.path.insert(0, os.path.expanduser('~/website'))
sys.path.insert(0, os.path.expanduser('~/virtualenv/website/3.12/lib/python3.12/site-packages'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'axmedova_project.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()