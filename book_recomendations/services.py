# recommendations/services.py
import requests
from .models import Book

def fetch_books_from_google(query, max_results=10):
    api_url = f"https://www.googleapis.com/books/v1/volumes?q={query}&maxResults={max_results}"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    return None

def get_or_create_books(query, max_results=10):
    books_data = fetch_books_from_google(query, max_results)
    books = []
    if books_data:
        for item in books_data.get('items', []):
            volume_info = item.get('volumeInfo', {})
            book, created = Book.objects.get_or_create(
                google_books_id=item.get('id'),
                defaults={
                    'title': volume_info.get('title', ''),
                    'description': volume_info.get('description', ''),
                    'categories': ', '.join(volume_info.get('categories', [])),
                    'cover_url': volume_info.get('imageLinks', {}).get('thumbnail', ''),
                }
            )
            books.append(book)
    return books
