from rest_framework.views import APIView
from rest_framework.response import Response

from books.serializers.book_serializer import BookSerializer
from books.services.book_service import BoookService

class BookCreateAPIView(APIView):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.book_service = BoookService()


    def get(self, request):
        books = self.book_service.get_all_books()
        serializer = BookSerializer(books, many=True)
        return Response(data=serializer.data)
