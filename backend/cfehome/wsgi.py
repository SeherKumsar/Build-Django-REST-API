"""
WSGI config for cfehome project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
from dotenv import load_dotenv

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cfehome.settings')

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))  # load .env file

application = get_wsgi_application()