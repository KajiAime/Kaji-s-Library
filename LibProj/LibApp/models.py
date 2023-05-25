from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    publication_date = models.DateField(blank=True, null=True)
    isbn = models.CharField(max_length=13, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)

class Borrower(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=200)

class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(blank=True, null=True)