from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .services import get_or_create_books

@require_GET
def search_books(request):
    query = request.GET.get('query', '')
    if query:
        books = get_or_create_books(query)
        books_data = [
            {
                'id': book.id,
                'title': book.title,
                'description': book.description,
                'categories': book.categories,
                'cover_url': book.cover_url
            }
            for book in books
        ]
        return JsonResponse(books_data, safe=False)
    return JsonResponse({'error': 'No query provided'}, status=400)


def hello(request):
    return JsonResponse({'message': 'Hello from Django!'})
