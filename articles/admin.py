from django.contrib import admin
from articles.models import Article, FavouriteArticle


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published_at']
    search_fields = ['title', 'author']


class FavouriteArticleAdmin(admin.ModelAdmin):
    list_display = ['article', 'account']


admin.site.register(Article, ArticleAdmin)
admin.site.register(FavouriteArticle, FavouriteArticleAdmin)
