from django.contrib import admin
from articles.models import Article, FavouriteArticle

admin.site.register(Article)
admin.site.register(FavouriteArticle)
