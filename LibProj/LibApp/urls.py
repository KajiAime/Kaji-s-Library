from django.urls import path
from .views import BookListView, BookCreateView, BookUpdateView, BorrowerCreateView, BorrowerUpdateView, LoanCreateView, LoanUpdateView

urlpatterns = [
    path('api/books/', BookCreateView.as_view(), name='book-create'),
    path('api/books/<int:pk>/', BookUpdateView.as_view(), name='book-update'),
    path('books/', BookListView.as_view(), name='book-list'),    
    path('api/borrowers/', BorrowerCreateView.as_view(), name='borrower-create'),
    path('api/loans/', LoanCreateView.as_view(), name='loan-create'),
    path('api/loans/<int:pk>/', LoanUpdateView.as_view(), name='loan-update'),
]