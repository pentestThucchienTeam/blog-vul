from django.db import models

# Create your models here.
from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField
from django.db.models.fields.related import  OneToOneField

# Create your models here.
class Tags(models.Model):
    title = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.title


class catalogies(models.Model):
    title = CharField(max_length=50)
    def __str__(self):
        return self.title