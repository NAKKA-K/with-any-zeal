import os
import environ

env = environ.Env()

DEFAULT_FROM_EMAIL = env('EMAIL_NAME')

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = env('EMAIL_NAME')
EMAIL_HOST_PASSWORD = env('EMAIL_PASS')
EMAIL_USE_TLS = True
