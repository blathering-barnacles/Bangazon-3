from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from bangazon import views


router = DefaultRouter()
router.register('productTypes', views.ProductTypeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]