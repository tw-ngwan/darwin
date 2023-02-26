import os
from django.core.asgi import get_asgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dashboard_master.settings')

application = StaticFilesHandler(get_asgi_application())
