"""
ASGI config for Dog_Breed_Identification_Using_Deep_Learning project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Dog_Breed_Identification_Using_Deep_Learning.settings')

application = get_asgi_application()
