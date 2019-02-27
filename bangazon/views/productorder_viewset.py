from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework import filters

from bangazon.models import ProductOrder
from bangazon.serializers import ProductOrderSerializer

@api_view(['GET'])
def api_root(request, format=None):
  return Response({
    'productorder': reverse('productorder', request=request, format=format),
  })

class ProductOrderViewSet(viewsets.ModelViewSet):
  queryset = ProductOrder.objects.all()
  serializer_class = ProductOrderSerializer

#   filter_backends = (filters.SearchFilter,)
#   search_fields = ('title', 'year')