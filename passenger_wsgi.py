"""
WSGI configuration for deployment on cPanel with Passenger.

This file is specifically for cPanel/Passenger deployment.
Replace the placeholder paths with your actual server paths.
"""

import os
import sys

# IMPORTANT: Update these paths to match your cPanel setup
# Example: /home/username/public_html/axmedova
INTERP = os.path.expanduser("~/public_html/axmedova/venv/bin/python")
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

# Add your project directory to the sys.path
sys.path.insert(0, os.path.expanduser('~/public_html/axmedova'))
sys.path.insert(0, os.path.expanduser('~/public_html/axmedova/venv/lib/python3.9/site-packages'))

# Set Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'axmedova_project.settings'

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

