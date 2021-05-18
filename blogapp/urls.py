from django.urls import path
from blogapp import views

urlpatterns = [
    path('', views.index, name="blogindex"),
    path('post', views.post, name="post"),
    path('blog', views.blog, name="blog"),

]
