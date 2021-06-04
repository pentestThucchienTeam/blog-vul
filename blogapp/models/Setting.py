from django.db import models
from django.forms.fields import BooleanField


class Vul (models.Model):
    XSS = (("Yes","Yes"),
            ("No", "No"))
    CSRF = (("Yes","Yes"),
            ("No", "No"))
 
    XSS = models.CharField(max_length=4, choices=XSS, default='No')
    CSRF = models.CharField(max_length=4, choices=CSRF, default='No')

    def __str__(self):
        return f'XSS {self.XSS}'+'--'+f'CSRF {self.CSRF}'


# class Vul(models.Model):
#     XSS = models.BooleanField(default=False, blank=True)
#     CSRF = models.BooleanField(default=False, blank=True)


    class Meta:
        verbose_name_plural="Vul"

    