from django.contrib import admin
from django.urls import path,re_path
from . import views

urlpatterns = [
    path('/', views.articles_list, name='list'),
    path('/<slug>/', views.article_detail, name='detail')
    # re_path(r'^(?P<slug>[\w-]+)/$', views.article_detail)
]
