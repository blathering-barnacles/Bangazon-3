from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework import filters

from bangazon.models import Employee, Department, ComputerEmployee
from bangazon.serializers import EmployeeSerializer

@api_view(['GET'])
def api_root(requst, format=None):
  return Response({
        'employees': reverse('employees', request=request, format=format)
    })

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    http_method_names = ['get', 'post', 'put']




