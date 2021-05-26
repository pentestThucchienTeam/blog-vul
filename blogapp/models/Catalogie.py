from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField
from django.db.models.fields.related import  OneToOneField


class Catalogies(models.Model):
    title = CharField(max_length=50)
    def __str__(self):
        return self.title