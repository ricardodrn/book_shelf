
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20, unique=True)
    publication_date = models.DateField()
    genre = models.CharField(max_length=50)
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    status = models.CharField(max_length=20, default='available', choices=[
        ('available', 'Available'),
        ('checked_out', 'Checked Out'),
        ('lost', 'Lost'),
        ('damaged', 'Damaged'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} by {self.author}"