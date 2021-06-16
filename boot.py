import os
import django
from django.conf import settings

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "farmer"))

def boot_django():
    settings.configure(
        BASE_DIR=BASE_DIR,
        DEBUG=True,
        DATABASES = {
           'default': {
                'ENGINE': 'django.db.backends.mysql', 
                'NAME': 'agrostardb',
                'USER': 'root',
                'PASSWORD': 'password',
                'HOST': 'localhost',   
                'PORT': '3306',
             }
     

         },
        INSTALLED_APPS=(
            "farmer",
        ),
        TIME_ZONE="UTC",
        USE_TZ=True,
    )
    django.setup()