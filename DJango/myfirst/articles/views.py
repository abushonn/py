from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Article, Comment

from django.urls import reverse
#
# def index(request):
#     return HttpResponse("Hello, world!!!")
#

def test(request):
    return HttpResponse("Hello, TEST!!!")

def index(request):
    latest_articles_list = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'articles/list.html', {'latest_articles_list' :latest_articles_list})


def detail(request, article_id):
    try:
        a= Article.objects.get(id= article_id)
    except:
        raise Http404("Article not found!")

    latest_comments_list = a.comment_set.order_by('-id')[:10]

    return render(request, 'articles/detail.html', {'article': a, 'latest_comments_list' : latest_comments_list})

def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Article not found!")

    a.comment_set.create(author_name = request.POST['name'], comment_text=request.POST['text'])

    return HttpResponseRedirect(reverse('articles:detail', args=(a.id, )))