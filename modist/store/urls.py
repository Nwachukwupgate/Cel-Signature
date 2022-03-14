from . import views
from django.urls import path
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name = 'home page'),
    path('shop', views.shop, name = 'shop'),
    url(r'^(?P<link_id>[0-9]+)/$', views.details, name = 'details'),

    path('cart', views.cart, name = 'cart'),
    path('checkout', views.checkout, name = 'checkout'),
    path('update_item/', views.updateItem, name = 'update_item')
]

