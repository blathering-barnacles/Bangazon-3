from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from bangazon.models import ProductType
from bangazon.serializers import ProductTypeSerializer
from django.shortcuts import render
from rest_framework import filters


# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'Types': reverse('Types', request=request, format=format),
#     })


class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'deletedOn')

    # def get_queryset(self):
    #     query_set = Movie.objects.all()
    #     # when a dictionary you can use get to search for something and if its not there you can give it
    #     # a default value of None or anything else
    #     keyword = self.request.query_params.get('search', None)
    #     if keyword is not None:
    #         print("query params", keyword)
    #         query_set = query_set.filter(title__icontains=keyword)
    #     return query_set