from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^categories/?$', views.CategoryList.as_view(), name='categories'),
        url(r'^category/(?P<name>[\w ]+)/?$', views.CategoryView.as_view(), name='category'),
        url(r'^item/(?P<title>[\w ]+)/?$', views.ItemView.as_view(), name='item'),
        ]
