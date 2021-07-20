from django.views.generic.base import TemplateView
from blogapp.views.form_register import RegistrationForm
from django.shortcuts import render,redirect
import time
from blogapp.views.validate import validate


class register(TemplateView):
    template_name = 'blogapp/register.html'

    def get(self, request):
        form = RegistrationForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = RegistrationForm(request.POST)

        if form.is_valid():
            validate.clean_password2(form)
            validate.clean_username(form)
            form.save()
            return redirect('/login')
        args = {'form': form, 'text': 'Success'}
        return render(request, self.template_name, args)
        


