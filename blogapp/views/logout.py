from django.contrib.auth import logout
from django.conf import settings
from django.shortcuts import redirect
from django.views.generic.base import TemplateView


class logoutView(TemplateView):
    template_name = "login.html"

    def get(self, request):
        logout(request)
        response = redirect(settings.LOGOUT_REDIRECT_URL)
        response.delete_cookie("auth")
        return response
