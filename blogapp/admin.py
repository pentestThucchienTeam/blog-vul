from blogapp.models.tag import Tags
from blogapp.models.Comment import Comment
from blogapp.models.Post import Post
from blogapp.models.User import user
from blogapp.models.UserProfile import userprofile
from django.contrib import admin


admin.site.register(Tags)
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(userprofile)
admin.site.register(user)
