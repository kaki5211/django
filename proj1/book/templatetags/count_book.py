from django import template
from book.models import Book

register = template.Library()

@register.filter
def count_books(value):
    count_book = Book.objects.filter(Author_info__author=value).count()
    return count_book
