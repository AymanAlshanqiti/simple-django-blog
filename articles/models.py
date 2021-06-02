from django.db import models

# Create your models here.


class Article(models.Model):
    source_id = models.CharField(max_length=64, blank=True)
    source_name = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    title = models.CharField(max_length=128)
    description = models.TextField()
    url = models.CharField(max_length=256)
    url_to_image = models.CharField(max_length=256)
    published_at = models.DateTimeField(auto_now_add=False)
    content = models.TextField()

    def __str__(self):
        return self.title
