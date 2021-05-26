from blogapp.models.Tag import Tags
from blogapp.models.Role import Role
from blogapp.models.Comment import Comment
from blogapp.models.Post import Post
from blogapp.models.Userprofile import Userprofile
from django.contrib import admin


admin.site.register(Tags)
admin.site.register(Role)

class Commentadmin(admin.ModelAdmin):
    list_display = ['content', 'admin_photo']
    readonly_fields = ('admin_photo',)
admin.site.register(Comment, Commentadmin)    
class Postadmin(admin.ModelAdmin):
    list_display=['title','creat_time', 'content', 'admin_photo']    
    list_filter = ['creat_time']
    readonly_fields = ('admin_photo',)
admin.site.register(Post, Postadmin)

admin.site.register(Userprofile)
