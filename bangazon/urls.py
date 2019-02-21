from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from bangazon import views

router = DefaultRouter()
router.register('computers', views.ComputerViewSet,)
router.register('products', views.ProductViewSet,)
router.register('customers', views.CustomerViewSet,)
router.register('productTypes', views.ProductTypeViewSet)


urlpatterns = [
    path('api/v1/', include(router.urls))
]