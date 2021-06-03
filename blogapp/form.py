from django import forms

XSS = (
    ("1", "Yes"),
    ("2", "No"),
)
CSRF = (
     ("1", "Yes"),
    ("2", "No"),
)
class Vul(forms.Form):
    XSS=forms.ChoiceField(choices=XSS)
    CSRF=forms.ChoiceField(choices=CSRF)