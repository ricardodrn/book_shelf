from django.urls import path
from books.views import BookCreateAPIView, BookRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('books/', BookCreateAPIView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view(), name='book-retrieve-update-destroy'),
]