from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Category, Transaction
from .serializers import CategorySerializer, TransactionSerializer

# This will control Category endpoints
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# This will control Transaction endpoints
class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "message": "Welcome to Budget Tracker API 👋",
        "endpoints": {
            "Categories": "/api/categories/",
            "Transactions": "/api/transactions/"
        }
    })

from django.shortcuts import render
from rest_framework import viewsets
from .models import Category, Transaction
from .serializers import CategorySerializer, TransactionSerializer

# API Views
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

# Homepage (HTML)
def home(request):
    return render(request, "tracker/home.html")
