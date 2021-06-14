from blogapp.models.Tag import Tags
from blogapp.models.Role import Role
from blogapp.models.Comment import Comment
from blogapp.models.Post import Post
from blogapp.models.Userprofile import Userprofile
from blogapp.models.Setting import Vul
from django.contrib import admin


admin.site.register(Tags)
admin.site.register(Role)

class Commentadmin(admin.ModelAdmin):
    list_display = ['create_time','admin_content', 'cmt_image',]
    list_filter = ['create_time']
    readonly_fields = ('cmt_image',)
    def cmt_image(self, obj):
            return obj.cmt_image

    cmt_image.short_description = 'images'
    cmt_image.allow_tags = True

admin.site.register(Comment, Commentadmin)  

class CommentInline(admin.StackedInline):
    model = Comment
    fields=["author_id","content"]
class Postadmin(admin.ModelAdmin):
    list_display = ['title','creat_time', 'admin_content','post_images',]
    list_filter = ['creat_time']
    readonly_fields = ('post_images',)
    inlines = [CommentInline]
    def post_images(self, obj):
            return obj.post_images

    post_images.short_description = 'images'
    post_images.allow_tags = True

admin.site.register(Post, Postadmin)

admin.site.register(Userprofile)
class vuladmin(admin.ModelAdmin):
    list_display = ['name','status', ]
admin.site.register(Vul,vuladmin)
