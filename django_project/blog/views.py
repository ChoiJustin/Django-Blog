# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

posts = [
    {
        'author': 'JustinChoi',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'data_posted': 'July 5, 2019'
    },
    {
        'author': 'NicoleSu',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'data_posted': 'July 6, 2019'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
