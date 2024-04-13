from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
from django.contrib.auth.decorators import login_required
from .models import Article
import json

from .util import get_prev_next_id, get_context
import code
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
   
    prev_id, current_id, next_id = get_prev_next_id(id)

    return render(request, 'blog/post.html', context=get_context(prev_id, current_id, next_id))
     #, "next_id": next_id, "next_title": next_title, "prev_id": prev_id, "prev_title": prev_title})

def about(request):
    return render(request, 'blog/about.html')

@login_required
def write(request):
    return render(request, 'blog/write.html')

@login_required
def create_article(request):
    print("creating article")

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        article = Article(title=title, content=content)
        article.save()

        return HttpResponse('Article sumitted successfully')
    else:
        return HttpResponseNotAllowed(['POST'])