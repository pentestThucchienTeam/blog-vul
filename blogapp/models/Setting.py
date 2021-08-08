from django.db import models
from django.db.models.fields import CharField
from django.forms.fields import BooleanField


class Vul(models.Model):
    name = models.CharField(
        max_length=20,
    )
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name
