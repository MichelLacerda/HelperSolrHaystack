# -*- coding: utf-8 -*-
# from datetime import datetime
from haystack import indexes
from project.core.models import Book


class BookIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    pub_date = indexes.DateField(model_attr='pub_date')

    def get_model(Self):
        return Book

    def index_queryset(self, using=None):
        """Atualiza indices"""
        return self.get_model().objects.all()
