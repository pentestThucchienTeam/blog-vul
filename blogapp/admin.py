from .models import Post, Tags
from .models import Profile
from .models import Comment
from .models import Tags

from django.contrib import admin
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Tags)
