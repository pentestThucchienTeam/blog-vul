from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField


class Tags(models.Model):
    name = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.name
