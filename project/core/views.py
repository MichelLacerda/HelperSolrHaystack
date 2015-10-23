# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import Http404
from project.core.models import Book
from haystack.query import SearchQuerySet


# def index(request):
#     try:
#         book = Book.objects.get(pk=1)
#     except:
#         raise Http404("Book não existe")
#
#     return render_to_response('core/index.html', {'book': book})
#

def search(request):
    books = SearchQuerySet().\
        autocomplete(content_auto=request.POST.get('search_text', ''))
    return render_to_response('core/search.html', {'books': 'books'})
