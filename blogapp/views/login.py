import jwt
import time
from core.lib.jwt_vul.get_key import get_key
from django.shortcuts import render, redirect
from .login_form import LoginForm
from blogapp.models.Setting import Vul
from django.contrib.auth import authenticate, login
from django.utils.http import http_date
from decouple import config
from django.views.generic import TemplateView
from .validate import validate
from django.http.response import Http404


def create_cookie(user, request):
    jwt_confusion = Vul.objects.filter(name="JWT_Key_Confusion").values()[0]["status"]
    jwts = Vul.objects.filter(name="JWT").values()[0]["status"]

    is_admin = user.is_superuser
    username = user.username
    payload = {"username": username, "admin": is_admin}

    if jwt_confusion and not jwts:

        from core.lib import jwt_vul

        with open(config("PRIVATEKEY"), "r") as filekey:
            privatekey = filekey.read()

        with open(config("PUBLICKEY"), "r") as pubkey:
            embedded = pubkey.read()

        return jwt_vul.encode(payload, privatekey, algorithm="RS256", headers={"publickey": embedded}).decode()

    elif jwts:
        from core.lib import jwt_vul

        key = get_key.weak()
        request.session["key"] = key

        return jwt_vul.encode(payload, key, algorithm="HS256").decode()

    else:
        key = get_key.secrure()
        request.session["key"] = key

        return jwt.encode(payload, key, algorithm="HS256")


class loginView(TemplateView):
    template_name = "login.html"

    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        msg = None
         
        safe_redirect = self.request.GET.get("next")
        openRedirect = Vul.objects.get(name="Open Redirect").status
        if not openRedirect:
            if not validate.safe_url(safe_redirect):
                raise Http404
       

        
        if form.is_valid():
            username = form["username"].value()
            password = form["password"].value()
            user = authenticate(username=username, password=password)

            if user:
                login(self.request, user)

                cookie_name = create_cookie(user, self.request)
                try:
                    max_age = self.request.session.get_expiry_age()
                    expires_time = time.time() + max_age
                    expires = http_date(expires_time)
                    response = redirect(safe_redirect)
                    response.set_cookie("auth", cookie_name, max_age=max_age, expires=expires)
                    return response
                except:
                    max_age = self.request.session.get_expiry_age()
                    expires_time = time.time() + max_age
                    expires = http_date(expires_time)
                    response = redirect("/")
                    response.set_cookie("auth", cookie_name, max_age=max_age, expires=expires)
                    return response

            else:
                msg = "Username, password meo dung"
                return render(request, self.template_name, {"form": form, "msg": msg})

        else:
            msg = "Username, password meo dung"
            return render(request, self.template_name, {"form": form, "msg": msg})
