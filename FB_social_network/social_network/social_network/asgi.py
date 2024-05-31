"""
ASGI config for social_network project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import Get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_network.settings')

application = Get_asgi_application()