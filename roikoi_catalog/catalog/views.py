from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse('test test')


def catalog_item(request, path):
    path = path.split('/')
    if len(path) == 1:
        return catalog_category(request, path[0])
    return HttpResponse(' '.join(slug.split('/')))
