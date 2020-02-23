"""
WSGI config for itm project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

import elasticsearch_dsl

from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'itm.settings')

elastic = elasticsearch_dsl \
    .connections \
    .create_connection(alias='default', hosts=[os.getenv('ELASTIC_HOST', '127.0.0.1')])

application = get_wsgi_application()
