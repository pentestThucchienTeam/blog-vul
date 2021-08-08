from django.views.generic.base import TemplateView
from .register_form import RegistrationForm
from django.shortcuts import render
from .validate import validate
from blogapp.models.Setting import Vul


class registerView(TemplateView):
    template_name = "register.html"

    def get(self, request):
        form = RegistrationForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            ssti = Vul.objects.filter(name="SSTI").values()[0]["status"]
            if ssti:
                validate.clean_password2(form)
                form.save()
            else:
                validate.clean_password2(form)
                validate.clean_username(form)
                form.save()
        args = {"form": form, "text": "Success"}
        return render(request, self.template_name, args)
