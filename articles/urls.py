from django.urls import path
from articles import views

urlpatterns = [
    path('articles/', views.articles_list, name='articles_list'),
    path('articles/<int:article_id>', views.article_detail, name='article_detail'),
]
