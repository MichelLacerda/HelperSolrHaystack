# -*- coding: utf-8 -*-
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        self.name


class Book(models.Model):
    author = models.ForeignKey(Author)
    title = models.CharField(max_length=255)
    pub_date = models.DateField(default=None)
    update_at = models.DateField(auto_now=True)

    def __unicode__(self):
        return self.title
