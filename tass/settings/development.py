from .base import *
from decouple import config

# DATABASES = {
# 	'default': {
# 	    'ENGINE': 'django.db.backends.postgresql_psycopg2',
# 		'NAME': 'tass',
#         'USER': 'postgres',
#         'PASSWORD': '147896321',
#         'HOST': 'localhost',
#         'PORT': '',
# 	}
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
