from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.generic import ListView, View

from .models import Category, Item

# Create your views here.


def index(request):
    return HttpResponse('test test')


def item_view(request, title):
    return HttpResponse("it's a {}!".format(item.title))


def category_view(request, name):
    return HttpResponse("category: {}".format(category.name))


class CategoryList(View):
    model = Category
    template_name = 'categories.html'

    def get(self, request):
        return render(request, self.template_name,
                      {'top_level_categories': Category.objects.filter(parent__isnull=True)})


class CategoryView(View):
    template_name = 'category.html'

    def get(self, request, name):
        try:
            cat = Category.objects.get(name=name)
        except Category.DoesNotExist:
            raise Http404('Category does not exist')
        else:
            ctx = {'category': cat,
                   'items': Item.objects.filter(category=cat).all()}
            return render(request, self.template_name, ctx)


class ItemView(View):
    template_name = 'item.html'

    def get(self, request, title):
        try:
            item = Item.objects.get(title=title)
        except Item.DoesNotExist:
            raise Http404('Item does not exist')
        else:
            ctx = {'item': item}
            return render(request, self.template_name, ctx)


