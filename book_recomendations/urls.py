from django.urls import path
from . import views
from .views import search_books

urlpatterns = [
    path('search/', search_books, name='search_books'),
    path('list-books/',
         views.ListBooks.as_view(),
         name="books")
]
