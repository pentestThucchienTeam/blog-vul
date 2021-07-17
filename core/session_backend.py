from django.contrib.sessions.backends.cache import SessionStore as OriginalSessionStore
from django.utils.crypto import get_random_string
from django.utils.module_loading import import_string
from django.utils.functional import cached_property
import string
from blogapp.models.Setting import Vul

VALID_KEY_CHARS = string.ascii_lowercase + string.digits

class SessionStore(OriginalSessionStore):
    jwt = Vul.objects.filter(name="JWT").values()[0]['status']

    def create_jwt(self):
        if self.jwt:
            from .lib import jwt_vul
            key = get_random_string(10, VALID_KEY_CHARS)
            return jwt_vul.encode({"key": key}, "password", algorithm="HS256").decode()
        else:
            import jwt
            key = get_random_string(10, VALID_KEY_CHARS)
            return jwt.encode({"key": key}, "secrect", algorithm="HS256")

    def _get_new_session_key(self):
        "Returns session key that isn't being used."
        while True:
            session_key = self.create_jwt()
            if not self.exists(session_key):
                break
        return session_key
