from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework import filters

from bangazon.models import ComputerEmployee
from bangazon.serializers import ComputerEmployeeSerializer

@api_view(['GET'])
def api_root(requst, format=None):
  return Response({
        'computerEmployee': reverse('computerEmployee', request=request, format=format)
    })

class ComputerEmployeeViewSet(viewsets.ModelViewSet):
    queryset = ComputerEmployee.objects.all()
    serializer_class = ComputerEmployeeSerializer
    http_method_names = ['get', 'post', 'put']