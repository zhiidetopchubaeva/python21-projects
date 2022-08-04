
from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import ProductViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls))
]