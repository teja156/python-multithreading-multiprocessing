import hashlib

import django
from django.conf import settings
from django.contrib.auth.hashers import make_password, check_password


# Configure Django settings module
settings.configure()

# Set up Django
django.setup()


def DjangoSHA256(password):
    return make_password(password)

def DjangoCheckSHA256(password, hash):
    return check_password(password, hash)

def SHA256(password):
    return hashlib.sha256(password.encode()).hexdigest()

# print(SHA256("golf032323762"))

# print(DjangoSHA256("imissu"))

# print(DjangoCheckSHA256("imissu","pbkdf2_sha256$600000$v3L28ciTbVElLkvJ6vVY6H$ifTK7S4OWDK80HHtsiGxeoq78o4v+x9Tnoyq0ksyg2g="))