from django import forms
from django.contrib.auth.models import User
from blogapp.models.Role import Role
from blogapp.models.Userprofile import Userprofile


class RegistrationForm(forms.Form):
    username = forms.CharField(
        label="Username", max_length=None, widget=forms.TextInput(attrs={"placeholder": "Username"})
    )
    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={"placeholder": "Email"}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"placeholder": "Password"}))
    password2 = forms.CharField(label="Re-password", widget=forms.PasswordInput(attrs={"placeholder": "Re-password"}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self):
        User.objects.create_user(
            username=self.cleaned_data["username"],
            email=self.cleaned_data["email"],
            password=self.cleaned_data["password1"],
        )

        Userprofile.objects.create(
            user=User.objects.get(username=self.cleaned_data["username"]),
            email=User.objects.get(username=self.cleaned_data["username"]),
            first_name="first_name",
            last_name="last_name",
            phone="phone",
            address="address",
            facebook="facebook",
            github="github",
            twitter="twitter",
            role=Role.objects.get(name="user_role"),
            avatar="",
        )
