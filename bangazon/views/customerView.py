from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework import filters

from bangazon.models import Product
from bangazon.serializers import ProductSerializer, CustomerSerializer 


@api_view(['GET'])
def api_root(requst, format=None):
  return Response({
        'customers': reverse('customers', request=request, format=format)
    })


  class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Cusotmer.objects.all()
    serializer_class = CustomerSerializer