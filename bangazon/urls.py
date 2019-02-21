from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from bangazon import views

router = DefaultRouter()
router.register('employees', views.EmployeeViewSet)
router.register('departments', views.DepartmentViewSet)
router.register('productTypes', views.ProductTypeViewSet)
router.register('computers', views.ComputerViewSet,)

urlpatterns = [
    path('api/v1/', include(router.urls))
]