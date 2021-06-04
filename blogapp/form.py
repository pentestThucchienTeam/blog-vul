from django.forms import fields
from blogapp import models
from blogapp.models.Setting import Vul
from django import forms

# XSS = (
#     ("1", "Yes"),
#     ("2", "No"),
# )
# CSRF = (
#      ("1", "Yes"),
#     ("2", "No"),
# )
# class Vul(forms.Form):
#     XSS=forms.ChoiceField(choices=XSS)
#     CSRF=forms.ChoiceField(choices=CSRF)
 
class Vul(forms.ModelForm):
    class Meta:
        model = Vul
        fields=["XSS", "CSRF"]
