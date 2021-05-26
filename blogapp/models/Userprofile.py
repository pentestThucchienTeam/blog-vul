from django.db import models
from django.contrib.auth.models import User
from blogapp.models.Role import Role
from django.utils.translation import gettext as _



class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    email = models.OneToOneField(User, related_name='emails', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=15, default=None, null=True)
    last_name = models.CharField(max_length=10, default=None, null=True)
    phone = models.CharField(max_length=32, null=True, blank=True)
    avatar = models.ImageField(upload_to=None, null=True, blank=True)
    status = models.TextField(blank=True, max_length=200)
    address = models.CharField(max_length=255, null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    facebooke = models.URLField(blank=True)
    github = models.URLField(blank=True)
    twitter = models.URLField(blank=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')

   
    
    def set_avatar(self):
        avatar = self.avatar
        if not avatar:
            self.avatar='/static/assets/img/avatar.png'
    

    def __str__(self):
        return f'{self.user.username}  profile'