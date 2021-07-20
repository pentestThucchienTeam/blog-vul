import secrets
import string
from django.utils.crypto import get_random_string

VALID_KEY_CHARS = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

class secure():
    secure_key = get_random_string(32, VALID_KEY_CHARS)

class weak():
    with open("/code/text/key.txt","r") as file:
        weak_key =  secrets.choice(file.readlines())
