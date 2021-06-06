from django.db import models
from django.db.models.deletion import CASCADE
from account.models import Account


class Article(models.Model):
    source_name = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    title = models.CharField(max_length=128)
    description = models.TextField()
    url = models.CharField(max_length=256)
    url_to_image = models.CharField(max_length=512)
    published_at = models.DateTimeField(auto_now_add=False)
    content = models.TextField()

    def __str__(self):
        return self.title


class FavouriteArticle(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.account.email
