from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('shop/',views.shop, name='shop'),
    path('agents/',views.agents, name='agents'),
    path('blog/',views.blog, name='blog'),
    path('properties/',views.properties, name='properties'),
    path('list/',views.list, name='list'),
    path('grid/',views.grid, name='grid'),
]
