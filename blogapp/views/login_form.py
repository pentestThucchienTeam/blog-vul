from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        label=("Username"), widget=forms.TextInput(attrs={"placeholder": "username", "class": "form-field"})
    )

    password = forms.CharField(
        label=("Password"),
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "password",
                "class": "form-field",
            }
        ),
    )
