import os
from channels.routing import pro
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Empleado.settings')

application = get_asgi_application()
