from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

from .util import get_prev_next_id, get_context
# Create your views here.

def home(request):
    # get the most recent article and render into post template
    latest_article = Article.objects.last()

    prev_id, current_id, next_id = get_prev_next_id(latest_article.id) 
    return render(request, 'blog/post.html', get_context(prev_id, current_id, next_id))

def articles(request):
    # list all articles
    return render(request, 'blog/articles.html', {"articles" : Article.objects.all().order_by('-date')})

def article(request, id):
    # number_of_articles = Article.objects.count()
    # print(f"Number of articles: {number_of_articles}")
    # if id > 1:
    #     prev_id = id - 1
    # else:
    #     prev_id = number_of_articles

    # if id < number_of_articles:
    #     next_id = id + 1
    # else:
    #     next_id = 1

    # print(f"{prev_id=}") 
    # print(f"{next_id=}")
    # prev_art = Article.objects.filter(id=prev_id).first()
    # next_art = Article.objects.filter(id=next_id).first()
    prev_id, current_id, next_id = get_prev_next_id(id)

    return render(request, 'blog/post.html', context=get_context(prev_id, current_id, next_id))
     #, "next_id": next_id, "next_title": next_title, "prev_id": prev_id, "prev_title": prev_title})

def about(request):
    return render(request, 'blog/about.html')
