from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect
from .models import Article
import json

from .util import get_prev_next_id, get_context, get_prev_next_article_by_slug, convert_markdown
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

def article(request, slug):
    context = get_prev_next_article_by_slug(slug)

    return render(request, 'blog/post.html', context=context)
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

        converted_content = convert_markdown(content)

        article = Article(title=title, content=converted_content)
        article.save()

         # Display success message:
        messages.success(request, 'Article submitted successfully', extra_tags='alert-success')
        return redirect('blog-article', slug=article.slug)  # Redirect to the article detail page
    else:
        return HttpResponseNotAllowed(['POST'])

@login_required
def convert(request):
    print("Got conversion request")
    
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            markdown = data.get('markdown')

            print("Original markdown: ", markdown)
            conversion_result = convert_markdown(markdown)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    data = {'converted': conversion_result}
    return JsonResponse(data)