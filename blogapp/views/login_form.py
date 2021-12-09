from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        required = False,
        label = ("Username"), 
        widget = forms.TextInput(
            attrs = {
                "placeholder": "username", 
                "class": "form-field"
            }
        )
    )

    password = forms.CharField(
        required = False,
        label = ("Password"),
        widget = forms.PasswordInput(
            attrs={
                "placeholder": "password",
                "class": "form-field",
            }
        ),
    )
    rememberMe = forms.BooleanField(
        required = False,
        widget = forms.CheckboxInput(
            attrs = {
                "class": "form-field",
            }
        )
    )
