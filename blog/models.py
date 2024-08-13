from django.db import models
from django.utils import timezone


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField()
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING, null=True)

    def published_recently(self):
        return self.published_date >= timezone.now() - timezone.timedelta(days=7)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING, null=True)
    author_name = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField()

    def __str__(self):
        return self.author_name