from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=None,  widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(label='Email',widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label='Re-password', widget=forms.PasswordInput(attrs={'placeholder': 'Re-password'}))

    class Meta:
        model = User
        fields=("username", "email", "password1", "password2")

    def save(self):
         User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password1'])
    