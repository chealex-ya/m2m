from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article


def articles_list(request, ordering='-published_at'):
    template = 'articles/news.html'
    object_list = Article.objects.all()
    context = {
                'object_list' : object_list
    }

    return render(request, template, context)
