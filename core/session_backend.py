from django.contrib.sessions.backends.cache import SessionStore as OriginalSessionStore
from django.utils.crypto import get_random_string
from django.utils.module_loading import import_string
import string
from blogapp.models.Setting import Vul
import random
import jwt
from decouple import config

VALID_KEY_CHARS = string.ascii_lowercase + string.digits


class SessionStore(OriginalSessionStore):

    
    def create_jwt(self):
        broken = Vul.objects.filter(name="Broken Authencation").values()[0]["status"]
        if broken :
      
            key = "session" + str(random.randint(9999, 999999))
            return key

        else:

            pas = config("KEY")
            key = get_random_string(10, VALID_KEY_CHARS)
            q = jwt.encode({"key": key}, pas, algorithm="HS256")
            return q

    def _get_new_session_key(self):
        "Returns session key that isn't being used."
        while True:
            session_key = self.create_jwt()
            if not self.exists(session_key):
                break
        return session_key
