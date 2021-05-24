from tags.models import Tags
from gprofile.models import gprofile
from comment.models import Comment
from post.models import Post
from guser.models import guestuser
from django.contrib import admin


admin.site.register(Tags)
admin.site.register(gprofile)
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(guestuser)