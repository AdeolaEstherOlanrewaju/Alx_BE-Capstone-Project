from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User  # use built-in User model

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Transaction Model
class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ("income", "Income"),
        ("expense", "Expense"),
    )

    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.type} - {self.amount}"
