from django.contrib.auth.models import User
from django.db import models


class Author(User):
    pass


class Book(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(Author)
    isbn = models.CharField(max_length=300)
    resume = models.TextField()

    def __unicode__(self):
        return self.title
