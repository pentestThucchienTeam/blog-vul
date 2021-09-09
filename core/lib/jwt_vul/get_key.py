import secrets
import string
from django.utils.crypto import get_random_string

VALID_KEY_CHARS = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
class get_key():

    def secrure():
        secure_key = get_random_string(32, VALID_KEY_CHARS)
        return secure_key
    
    def weak():
        with open("text/key.txt","r") as file:
            weak_key =  secrets.choice(file.readlines()).strip()
        return weak_key