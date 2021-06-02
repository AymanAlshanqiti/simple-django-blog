from django.http.response import HttpResponse
from django.shortcuts import render
from articles.models import Article
from django.http import HttpResponse

# Create your views here.


def articles_list(request):
    articles = Article.objects.all()
    context = {"articles": articles}
    return render(request, 'articles_list.html', context)


def article_detail(request, article_id):
    article = Article.objects.get(id=article_id)
    context = {"article": article}
    return render(request, 'article_detail.html', context)
