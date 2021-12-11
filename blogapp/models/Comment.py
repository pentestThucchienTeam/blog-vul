from django.db import models
from blogapp.models.Post import Post
from blogapp.models.Userprofile import Userprofile
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe
from django.conf import settings


class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment")
    author_id = models.ForeignKey(Userprofile, on_delete=models.CASCADE, related_name="author_name")
    content = RichTextUploadingField(default="")
    status = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    email = models.ForeignKey(Userprofile, on_delete=models.CASCADE, related_name="author_email")
    image = models.ImageField(
        upload_to="uploads/%Y/%m/%d", height_field=None, width_field=None, max_length=100, blank=True
    )

    def __str__(self):
        return self.content

    def admin_content(self):
        return mark_safe(self.content)

    @property
    def cmt_image(self):
        if self.image:
            return mark_safe('<img src="{}" width="100" height="100" />'.format(self.image.url))
        return ""
