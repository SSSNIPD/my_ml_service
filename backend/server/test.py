import os

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
print(SECRET_KEY)