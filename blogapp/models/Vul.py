# blogapp/models/vul.py
from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField

# Create model vul
class Vul(models.Model):
    name = models.CharField(max_length=20, default='')
    status = models.BooleanField()


    def __str__(self):
        return self.name

