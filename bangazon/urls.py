from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from bangazon import views

router = DefaultRouter()

# single entry point
router.register('Products', views.ProductViewSet)

urlpatterns = [
  path('api/v1/', include(router.urls))
]