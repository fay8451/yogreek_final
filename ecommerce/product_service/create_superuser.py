import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'product_service.settings_prod')
django.setup()

from django.contrib.auth.models import User
from django.db import IntegrityError

def create_superuser():
    try:
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='Admin123!'
            )
            print('Superuser created successfully')
        else:
            print('Superuser already exists')
    except IntegrityError:
        print('Superuser already exists')
    except Exception as e:
        print(f'An error occurred: {e}') 