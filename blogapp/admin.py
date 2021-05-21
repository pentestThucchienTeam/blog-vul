from .models import Tags
from .models import Profile
from .models import Comment
from .models import Posts
from django.contrib import admin


admin.site.register(Tags)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Posts)