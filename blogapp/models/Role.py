from django.db import models
from django.db.models.fields import CharField

class Role(models.Model):
    name = CharField(max_length=20, default='')

    def __str__(self):
        return self.name