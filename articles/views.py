from django.shortcuts import redirect, render
from articles.models import Article


def home_view(request):
    return redirect('articles_list')


def articles_list_view(request):
    articles = Article.objects.all()
    context = {"articles": articles}
    return render(request, 'articles_list.html', context)


def article_detail_view(request, article_id):
    article = Article.objects.get(id=article_id)
    context = {"article": article}
    return render(request, 'article_detail.html', context)
