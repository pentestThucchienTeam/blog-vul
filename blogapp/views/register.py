from django.views.generic.base import TemplateView
from .register_form import RegistrationForm
from django.shortcuts import render,redirect
from blogapp.views.validate import validate
import time

class registerView(TemplateView):
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
        args = {'form': form,}
        return render(request, self.template_name, args)
        


