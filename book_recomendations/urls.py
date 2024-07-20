from django.urls import path
from . import views
from .views import search_books

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('search/', search_books, name='search_books'),
]
