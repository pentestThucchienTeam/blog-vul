from django.views.generic import ListView
from blogapp.models.Setting import Vul
from django.shortcuts import render
import json, jwt
from django.template import engines
from core.lib import jwt_vul
from core.lib.jwt_vul.utils import base64url_decode


class settingView(ListView):
    template_name = "setting.html"
    nameVuls = Vul.objects.values("name")

    def get(self, request):
        object_list = Vul.objects.all()
        ssti = Vul.objects.filter(name="SSTI").values()[0]["status"]
        if ssti:
            engine = engines["django"]
            request.user.username = engine.from_string(request.user.username).render()
            object_list = Vul.objects.all()
            return render(request, self.template_name, {"object_list": object_list})
        else:
            return render(request, self.template_name, {"object_list": object_list})

    def post(self, request):
        object_list = Vul.objects.all()
        jwt_confusion = Vul.objects.filter(name="JWT_Key_Confusion").values()[0]["status"]
        jwts = Vul.objects.filter(name="JWT").values()[0]["status"]
        if request.user.username:
            cookie_check = request.COOKIES["auth"]
            if jwt_confusion and not jwts:
                ext, fake = cookie_check.split(".", 1)
                header = base64url_decode(bytes(str(ext), "utf-8"))
                pubkey = json.loads(header.decode("utf-8"))
                publickey = pubkey["publickey"]
                cookie_decode = jwt_vul.decode(cookie_check, publickey)

            elif jwts:
                key = request.session["key"]
                cookie_decode = jwt_vul.decode(cookie_check, key)

            else:

                key = request.session["key"]
                cookie_decode = jwt.decode(cookie_check, key, algorithms="HS256")

            if cookie_decode["admin"]:

                for _vuls in self.nameVuls:

                    if request.POST[_vuls["name"]] == "yes":
                        Vul.objects.filter(name=_vuls["name"]).update(status=True)
                    else:
                        Vul.objects.filter(name=_vuls["name"]).update(status=False)

                return render(request, self.template_name, {"object_list": object_list, "msg": "Change is success!"})
            else:

                return render(
                    request, self.template_name, {"object_list": object_list, "msg": "You don't have permission"}
                )

        else:
            return render(
                request, self.template_name, {"object_list": object_list, "msg": "Please login to apply this change!"}
            )
