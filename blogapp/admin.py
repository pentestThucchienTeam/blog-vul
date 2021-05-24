from blogapp.models.Tag import Tags
from blogapp.models.Comment import Comment
from blogapp.models.Post import Post
from blogapp.models.User import User
from blogapp.models.Userprofile import Userprofile
from django.contrib import admin


admin.site.register(Tags)
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(Userprofile)
admin.site.register(User)
