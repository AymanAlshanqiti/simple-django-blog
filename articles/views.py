from django.shortcuts import redirect, render
from articles.models import Article


def home_view(request):
    return redirect('articles-list')


def articles_list_view(request):
    articles = Article.objects.all()
    context = {"articles": articles}
    return render(request, 'articles-list.html', context)


def article_detail_view(request, article_id):
    article = Article.objects.get(id=article_id)
    context = {"article": article}
    return render(request, 'article-detail.html', context)


def add_article_to_favourite(request, article_id):
    if request.user.is_authenticated:
        print('user authenticatted')

    else:
        return redirect('home')
