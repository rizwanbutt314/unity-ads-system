# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ads-listing',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': 5432
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'd8dl6sg3pm43lj',
#         'USER': 'qnckotbaopydaq',
#         'PASSWORD': '773a696b3afd81c85151943f45b0411dc8f1bdcd07aeccd0cc90d9849ddf5522',
#         'HOST': 'ec2-174-129-240-67.compute-1.amazonaws.com',
#         'PORT': 5432
#     }
# }


# Project Settings
FILES_PATH = '/home/rizwan/Downloads/mounted_volume/'
FILES_EXTENSION = ['.pdf', '.png', '.jpg', 'jpeg']
