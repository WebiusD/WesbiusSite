from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="blog-home"),
    path('articles', views.articles, name="blog-articles"),
    path('article/<int:id>', views.article, name="blog-article"),
    path('about', views.about, name="blog-about"),
    path('write', views.write, name="blog-write"),
    path('create', views.create_article, name="create-article"),
    path('convert', views.convert, name="convert"),
]