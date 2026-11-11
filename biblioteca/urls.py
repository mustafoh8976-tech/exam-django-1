from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name = 'home'),
    path('create_autor/',create_autor, name = 'create_autor'),
    path('delete_autor/<int:pk>/',delete_autor, name = 'delete_autor'),
    path('update_autor/<int:pk>/',update_autor, name = 'update_autor'),
    path('list_autor/',list_autor, name = 'list_autor'),
    path('create_book/',create_book, name = 'create_book'),
    path('delete_book/<int:pk>/',delete_book, name = 'delete_book'),
    path('update_book/<int:pk>/',update_book, name = 'update_book'),
    path('list_book/',list_book, name = 'list_book'),
    path('create_order/',create_order, name = 'create_order'),
    path('delete_order/<int:pk>/',delete_order, name = 'delete_order'),
    path('update_order/<int:pk>/',update_order, name = 'update_order'),
    path('list_order/',list_order, name = 'list_order'),
]
