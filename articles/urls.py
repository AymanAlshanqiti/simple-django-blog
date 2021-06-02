from django.urls import path
from articles import views

urlpatterns = [
    path('articles/', views.articles_list, name='articles_list'),
]
