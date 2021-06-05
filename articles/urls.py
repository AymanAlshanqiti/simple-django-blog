from django.urls import path
from articles import views

urlpatterns = [
    path('home', views.home_view, name='home'),
    path('', views.articles_list_view, name='articles-list'),
    path('<int:article_id>',
         views.article_detail_view, name='article-detail'),
    path('<int:article_id>/add-to-favourite',
         views.add_article_to_favourite, name='add-article-to-favourite')
]
