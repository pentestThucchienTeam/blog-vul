from django.http.response import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from .comment_form import CommentForm
from blogapp.models.Post import Post
from blogapp.models.Userprofile import Userprofile
from blogapp.models.Tag import Tags
from blogapp.models.Comment import Comment
from blogapp.models.Setting import Vul


class postView(TemplateView):

    template_name = "post.html"
    user_avater = ""
    user_comment = ""
    def get(self, request, id):
        form = CommentForm()
        postView.object_list = Post.objects.filter(status=1).order_by('-creat_time')[:5]
        postView.listtag = Tags.objects.all()
        postView.xss = Vul.objects.filter(name="XSS").values()[0]["status"]
        postView.sql = Vul.objects.filter(name="SQLI").values()[0]["status"]
        postView.listPost = list(Post.objects.values_list('id', flat=True))
        
        previousPost = postView.listPost.index(int(id)) - 1
        if previousPost < 0:
            postView.pre_post = get_object_or_404(Post, id=postView.listPost[0])
        else:
            postView.pre_post = get_object_or_404(Post, id=postView.listPost[previousPost])

        nextPost = postView.listPost.index(int(id)) + 1
        if nextPost >= len(postView.listPost):
            postView.next_post = get_object_or_404(Post, id=postView.listPost[-1])
        else:
            postView.next_post = get_object_or_404(Post, id=postView.listPost[nextPost])

        if self.sql:
            postView.post_render = Post.objects.raw("SELECT * FROM blogapp_post WHERE id = %s" %id)
            if postView.post_render.status != '1':
                raise Http404
            for x in  Post.objects.raw("SELECT * FROM blogapp_post_author_id WHERE post_id = %s" %id) :
                for y in Userprofile.objects.raw("SELECT * FROM blogapp_userprofile WHERE user_id = %s" %x.user_id):
                   postView.user_avater = y
                   break
            for u in Comment.objects.raw("SELECT p.id, p.content, p.author_id_id, p.create_time, a.avatar from blogapp_comment as p join blogapp_userprofile as a on p.author_id_id = a.user_id where p.post_id_id = %s" %id):
                postView.user_comment = u
                break
                    
        else:
            postView.post_render = get_object_or_404(Post, id=id)
            if postView.post_render.status != '1':
                raise Http404
            for x in  Post.objects.raw("SELECT * FROM blogapp_post_author_id WHERE post_id = %s",[id]) :
                for y in Userprofile.objects.raw("SELECT * FROM blogapp_userprofile WHERE user_id = %s",  [x.user_id]):
                    postView.user_avater = y
                    break
            for u in Comment.objects.raw("SELECT p.id, p.content, p.author_id_id, p.create_time, a.avatar from blogapp_comment as p join blogapp_userprofile as a on p.author_id_id = a.user_id where p.post_id_id = %s" %id):
                postView.user_comment = u
                break
          

        return render(
            request,
            self.template_name,
            {
                "object_list": self.object_list,
                "listtag": self.listtag,
                "post_render": self.post_render,
                "form": form,
                "xss": self.xss,
                "sql": self.sql,
                "pre_post": self.pre_post,
                "next_post": self.next_post,
                "user_avater":self.user_avater,
                "user_comment": self.user_comment
            },
        )

    def post(self, request, id):
        postView.object_list = Post.objects.filter(status=1).order_by('-creat_time')[:5]
        postView.listtag = Tags.objects.all()
        postView.xss = Vul.objects.filter(name="XSS").values()[0]["status"]
        postView.sql = Vul.objects.filter(name="SQLI").values()[0]["status"]
        postView.listPost = list(Post.objects.values_list('id', flat=True))

        previousPost = postView.listPost.index(int(id)) - 1
        if previousPost < 0:
            postView.pre_post = get_object_or_404(Post, id=postView.listPost[0])
        else:
            postView.pre_post = get_object_or_404(Post, id=postView.listPost[previousPost])

        nextPost = postView.listPost.index(int(id)) + 1
        if nextPost >= len(postView.listPost):
            postView.next_post = get_object_or_404(Post, id=postView.listPost[-1])
        else:
            postView.next_post = get_object_or_404(Post, id=postView.listPost[nextPost])

        if self.sql:
            postView.post_render = Post.objects.raw("SELECT * FROM blogapp_post WHERE id = %s" % id)
            if postView.post_render.status != '1':
                raise Http404
            for x in  Post.objects.raw("SELECT * FROM blogapp_post_author_id WHERE post_id = %s" %id):
                for y in Userprofile.objects.raw("SELECT * FROM blogapp_userprofile WHERE user_id = %s" %x.user_id):
                   postView.user_avater = y
                   break
            for u in Comment.objects.raw("SELECT p.id, p.content, p.author_id_id, p.create_time, a.avatar from blogapp_comment as p join blogapp_userprofile as a on p.author_id_id = a.user_id where p.post_id_id = %s" %id):
                postView.user_comment = u
               
                break
        else:
            postView.post_render = get_object_or_404(Post, id=id)
            if postView.post_render.status != '1':
                raise Http404
            for x in  Post.objects.raw("SELECT * FROM blogapp_post_author_id WHERE post_id = %s",[id]):
                for y in Userprofile.objects.raw("SELECT * FROM blogapp_userprofile WHERE user_id = %s",  [x.user_id]):
                    postView.user_avater = y
            for u in Comment.objects.raw("SELECT p.id, p.content, p.author_id_id, p.create_time, a.avatar from blogapp_comment as p join blogapp_userprofile as a on p.author_id_id = a.user_id where p.post_id_id = %s" %id):
                postView.user_comment = u
                print(u)
                break
          
                    
        author = Userprofile.objects.get(user=request.user)   
        form = CommentForm(data=request.POST, author_id=author, post_id=self.post_render, email=author)
        if form.is_valid():
            form.save()

        return render(
            request,
            self.template_name,
            {
                "object_list": self.object_list,
                "listtag": self.listtag,
                "post_render": self.post_render,
                "form": form,
                "xss": self.xss,
                "sql": self.sql,
                "pre_post": self.pre_post,
                "next_post": self.next_post,
                "user_avater":self.user_avater,
                "user_comment": self.user_comment
            },
        )
