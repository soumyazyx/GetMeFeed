from django.db import models


class Post(models.Model):
    title = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.title


class NASA(models.Model):
    link = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=200, null=True, blank=True)
    summary = models.TextField()
    added_ts = models.DateTimeField(auto_now_add=True)
    published = models.CharField(max_length=255)
    article_id = models.CharField(max_length=255)
    author_img_url = models.CharField(max_length=255, null=True, blank=True)
    article_img_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title
