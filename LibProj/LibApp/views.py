from rest_framework import generics
from .models import Book, Borrower, Loan
from .serializers import BookSerializer, BorrowerSerializer, LoanSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BorrowerCreateView(generics.CreateAPIView):
    queryset = Borrower.objects.all()
    serializer_class = BorrowerSerializer

class BorrowerUpdateView(generics.UpdateAPIView):
    queryset = Borrower.objects.all()
    serializer_class = BorrowerSerializer

class LoanCreateView(generics.CreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

class LoanUpdateView(generics.UpdateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer