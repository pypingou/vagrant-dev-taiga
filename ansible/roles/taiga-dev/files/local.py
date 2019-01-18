from .development import *


#########################################
## GENERIC
#########################################

DEBUG = True

#ADMINS = (
#    ("Admin", "example@example.com"),
#)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'taiga',
        'USER': 'taiga',
        'PASSWORD': 'changeme',
        'HOST': 'localhost',                        
        'PORT': '',
    }
}

SITES = {
    "api": {
       "scheme": "http",
       "domain": "0.0.0.0:8000",
       "name": "api"
    },
    "front": {
       "scheme": "http",
       "domain": "0.0.0.0:9001",
       "name": "front"
    },
}
