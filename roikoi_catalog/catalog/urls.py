from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^([\w/]+)', views.item_or_category, name='item'),
        ]
