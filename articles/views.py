from django.shortcuts import redirect, render
from articles.models import Article, FavouriteArticle
import requests
import datetime


def articles_generator(request):
    res = requests.get(
        'https://newsapi.org/v2/everything?q=tesla&from=2021-05-06&sortBy=publishedAt&apiKey=165f4c8876ae4a1981fbe7c2f231d443')
    json = res.json()
    for index in range(15):
        article = Article()
        article.source_name = json['articles'][index]['source']['name']
        if json['articles'][index]['author'] != None:
            article.author = json['articles'][index]['author']
        else:
            article.author = '-'
        article.title = json['articles'][index]['title']
        article.description = json['articles'][index]['description']
        article.url = json['articles'][index]['url']
        article.url_to_image = json['articles'][index]['urlToImage']
        article.published_at = json['articles'][index]['publishedAt']
        article.content = json['articles'][index]['content']
        article.save()
    return redirect('articles-list')


def home_view(request):
    return redirect('articles-list')


def articles_list_view(request):
    articles = Article.objects.all()
    favourite_articles = FavouriteArticle.objects.all()
    context = {"articles": articles, "favourite_articles": favourite_articles}
    return render(request, 'articles-list.html', context)


def article_detail_view(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.user.is_authenticated:
        favourite_article = FavouriteArticle.objects.filter(
            article=article, account=request.user)
        if favourite_article:
            favourite_article = True
        else:
            favourite_article = False
        context = {"article": article,  "favourite_article": favourite_article}
        return render(request, 'article-detail.html', context)
    else:
        context = {"article": article}
        return render(request, 'article-detail.html', context)


def add_article_to_favourite(request, article_id):
    if request.user.is_authenticated:
        article = Article.objects.get(id=article_id)
        favourite_article = FavouriteArticle.objects.filter(
            article=article, account=request.user)
        if favourite_article:
            favourite_article.delete()
            return redirect('article-detail', article_id)
        else:
            favourite_article = FavouriteArticle()
            favourite_article.article = article
            favourite_article.account = request.user
            favourite_article.save()
            return redirect('article-detail', article_id)
    else:
        return redirect('home')
