import os

DEFAULT_FROM_EMAIL = os.environ['EMAIL_NAME']

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ['EMAIL_NAME']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_PASS']
EMAIL_USE_TLS = True
