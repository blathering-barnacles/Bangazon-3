from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from bangazon.models import ProductType
from bangazon.serializers import ProductTypeSerializer
from django.shortcuts import render
from rest_framework import filters
from rest_framework import status


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'productTypes': reverse('productTypes', request=request, format=format),
    })


class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'deletedOn')
