from django.contrib.auth import login,authenticate
from django.http.response import HttpResponse
from blogapp.forms import RegistrationForm
from django.http import HttpResponseRedirect 
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from blogapp.views.login import login_view

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('/login')
        
    form=RegistrationForm
    return render(request, 'blogapp/register.html', {'form': form})


