from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Category, Item

# Create your views here.


def index(request):
    return HttpResponse('test test')


def item_or_category(request, path):
    path = path.split('/')
    terminal = path[-1]
    try:
        item = Item.objects.get(title=terminal)
    except Item.DoesNotExist:
        try:
            category = Category.objects.get(name=terminal)
        except Category.DoesNotExist:
            raise Http404
        else:
            return category_view(request, category)
    else:
        return item_view(request, item)


def item_view(request, item):
    return HttpResponse("it's a {}!".format(item.title))


def category_view(request, category):
    return HttpResponse("category: {}".format(category.name))


