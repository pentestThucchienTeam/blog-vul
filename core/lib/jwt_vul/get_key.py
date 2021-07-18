import secrets
import string
from django.utils.crypto import get_random_string

VALID_KEY_CHARS = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
class secure():
    def secure_key():
        secure_key = get_random_string(32, VALID_KEY_CHARS)
        return secure_key
    k = secure_key()
    print(k)



class weak():
    def weak_key():
        file = open("text/key.txt").readlines()
        weak_key = secrets.choice(file)
        return weak_key

    w = weak_key()
    print(w) 