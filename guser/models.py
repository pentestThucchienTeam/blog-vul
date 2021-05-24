from django.db import models

# Create your models here.
class guestuser(models.Model):
    username = models.CharField(max_length=30, default='')
    password = models.CharField(max_length=30, default='')
    email = models.EmailField(max_length=254, default='')

    def __str__(self):
        return self.username