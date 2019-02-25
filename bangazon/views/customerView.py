from django.db.models import Q
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework import filters

from bangazon.models import Customer
from bangazon.serializers import ProductSerializer, CustomerSerializer 


@api_view(['GET'])
def api_root(requst, format=None):
  return Response({
        'customers': reverse('customers', request=request, format=format)
    })

class CustomerViewSet(viewsets.ModelViewSet):
  queryset = Customer.objects.all()
  serializer_class = CustomerSerializer
  http_method_names = ['get', 'post', 'put']


  def get_queryset(self):
    query_set = Customer.objects.all()
    keyword = self.request.query_params.get('search', None)
    if keyword is not None:
      print("query params", keyword)
      query_set = query_set.filter(title__icontains=keyword)
    return query_set
