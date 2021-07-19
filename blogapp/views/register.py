from django.contrib.auth import login,authenticate
from django.http.response import HttpResponse
from django.views.generic.base import TemplateView
from .register_form import RegistrationForm
from django.http import HttpResponseRedirect 
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from .login import loginView


class registerView(TemplateView):
    template_name = 'register.html'

    def get(self, request):
        form = RegistrationForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.cleaned_data['username']
            form.cleaned_data['email']
            form.cleaned_data['password1']
            form.cleaned_data['password2']
            form.save()

        args = {'form': form, 'text': 'Success'}
        return render(request, self.template_name, args)
        


