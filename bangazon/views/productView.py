from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework import filters

from bangazon.models import Product
from bangazon.serializers import ProductSerializer

@api_view(['GET'])
def api_root(request, format=None):
  return Response({
    'products': reverse('products', request=request, format=format),
  })

class ProductViewSet(viewsets.ModelViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

  filter_backends = (filters.SearchFilter,)
  search_fields = ('title', 'year')
  