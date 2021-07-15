from django.contrib.auth import logout
from django.conf import settings
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    response = redirect(settings.LOGOUT_REDIRECT_URL)
    response.delete_cookie('ten')
    return response
