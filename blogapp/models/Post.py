from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField
from blogapp.models.Tag import Tags
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.conf import settings


class Post(models.Model):

    title = models.CharField(max_length=30, default="")
    tags = models.ManyToManyField(Tags)
    status = models.CharField(max_length=50, default="")
    content = RichTextUploadingField(blank=True)
    creat_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    author_id = models.ManyToManyField(settings.AUTH_USER_MODEL)
    images = models.ImageField(
        upload_to="uploads/%Y/%m/%d", height_field=None, width_field=None, max_length=100, blank=True
    )

    def __str__(self):
        return f"{self.title}"

    def admin_content(self):
        return mark_safe(self.content)

    def get_url(self):

        return reverse("post", args=[self.id])

    @property
    def post_images(self):
        if self.images:
            return mark_safe('<img src="{}" width="100" height="100" />'.format(self.images.url))
        return ""
