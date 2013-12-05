"""
WSGI config for rest_time project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rest_time.settings")
path = '/home/bbashong/rest_time/rest_time'
if path not in sys.path:
    sys.path.append(path)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
