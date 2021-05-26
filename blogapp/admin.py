from blogapp.models.Tag import Tags
from blogapp.models.Role import Role
from blogapp.models.Comment import Comment
from blogapp.models.Post import Post
from blogapp.models.Userprofile import Userprofile
from django.contrib import admin


admin.site.register(Tags)
admin.site.register(Role)
class Cmtadmin(admin.ModelAdmin):
    list_display=['content ','Post_id']  
admin.site.register(Comment)

class Postadmin(admin.ModelAdmin):
    list_display=['title','creat_time', 'content', 'images']    
admin.site.register(Post, Postadmin)

admin.site.register(Userprofile)
