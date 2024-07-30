from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .services import get_books
from rest_framework.generics import(
    ListAPIView
)
from .models import Book
from .serializers import BookSerializer

@require_GET
def search_books(request):
    query = request.GET.get('query', '')
    if query:
        books = get_books(query)
        books_data = [
            {
                'id': book.get('id'),
                'title': book['title'],
                'description': book['description'],
                'categories': book['categories'],
                'cover_url': book['cover_url']
            }
            for book in books
        ]
        return JsonResponse(books_data, safe=False)
    return JsonResponse({'error': 'No query provided'}, status=400)


class ListBooks(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
