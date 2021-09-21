from core.settings import ALLOWED_HOSTS
from django import forms
import re
from django.contrib.auth.models import User
from decouple import config

class validate:
    
    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password2
        raise forms.ValidationError("Mật khẩu không hợp lệ")    


    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError("Tên tài khoản có kí tự đặc biệt")
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("Tài khoản đã tồn tại")

    def safe_url(url):
        ALLOWED_HOSTS = config("ALLOWED_HOSTS")
        pattern = re.compile(r"(^[^:]+://)([^\.]+\.[^\.]+)")
        matched = re.match(pattern, url)
        if matched:
            if matched.group(2) in ALLOWED_HOSTS:
                return True
            else:
                 return False
        else:
            return True