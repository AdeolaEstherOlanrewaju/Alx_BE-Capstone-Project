from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from tracker.views import CategoryViewSet, TransactionViewSet, home  # 👈 import home here

# DRF Router for API
router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('', home, name='home'),   # 👈 homepage
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
