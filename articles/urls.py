from django.urls import path
from articles import views

urlpatterns = [
    path('home', views.home_view, name='home'),
    path('', views.articles_list_view, name='articles_list'),
    path('<int:article_id>',
         views.article_detail_view, name='article_detail'),
]
