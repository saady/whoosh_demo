from haystack import indexes
from .models import Book, Author


class BookIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='author')
    title = indexes.CharField(model_attr='title')
    isbn = indexes.CharField(model_attr='isbn')
    resume = indexes.CharField(model_attr='resume')

    def get_model(self):
        return Book


class AuthorIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    first_name = indexes.CharField(model_attr='first_name')

    def get_model(self):
        return Author
