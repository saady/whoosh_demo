from django.contrib import admin
from django import forms
from apps.search.models import Book, Author


class BookAdminForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class AuthorAdminForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    form = AuthorAdminForm


class BookAdmin(admin.ModelAdmin):
    """
    """
    list_display = ('title', 'author',)
    form = BookAdminForm



admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
