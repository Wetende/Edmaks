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
    path('shop_detail/<int:pk>/',views.shop_detail, name='shop_detail'),
    path('cart/',views.cart, name='cart'),

    # path('bookmark/', bookmark, name='bookmark'),
    path('add_cart/', views.add_cart, name='add_bookmark'),

    #Ajaxified / Js
    path('remove_cart/', views.remove_cart, name='remove_cart'),
    path('update_cart/', views.update_cart, name='update_cart'),

    


]
