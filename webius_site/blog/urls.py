from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="blog-home"),
    path('articles', views.articles, name="blog-articles"),
    path('article/<int:id>', views.article, name="blog-article"),
    path('about', views.about, name="blog-about"),
]