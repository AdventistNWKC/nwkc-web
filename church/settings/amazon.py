import os

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'wkcadventist'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# AWS_REGION = 

# AWS_S3_HOST = 's3.{}.amazonaws.com'.format(AWS)
AWS_S3_CUSTOM_DOMAIN = '{}.S3.amazonaws.com'.format(AWS_STORAGE_BUCKET_NAME)

AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400',}

AWS_STATIC_LOCATION = 'static'
AWS_PUBLIC_MEDIA_LOCATION = 'media'

AWS_PRIVATE_MEDIA_LOCATION = 'private-media'

STATIC_URL = 'https://{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, AWS_STATIC_LOCATION)
MEDIA_URL = 'https://{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, AWS_PUBLIC_MEDIA_LOCATION)

ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'