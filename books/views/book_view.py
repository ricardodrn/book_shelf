from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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
    
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            book = self.book_service.create_book(serializer.data)
            return Response(BookSerializer(book).data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookRetrieveUpdateDestroyAPIView(APIView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.book_service = BoookService()
    
    def get(self, request, pk):
        book = self.book_service.get_book_by_id(pk)
        if not book:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    def put(self, request, pk):
        book = self.book_service.get_book_by_id(pk)
        if not book:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            updated_book = self.book_service.update_book(pk, serializer.validated_data)
            return Response(BookSerializer(updated_book).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        success = self.book_service.delete_book(pk)
        if not success:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)