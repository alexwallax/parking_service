from django.urls import path, include
from rest_framework import DefaultRouter

from customers.views import CustomerViewSet

router = DefaultRouter()
router.register('customers', CustomerViewSet)

urlpatters = [
    path('', include(router.urls)),
]