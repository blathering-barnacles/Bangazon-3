from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework import filters

from bangazon.models import Department
from bangazon.serializers import DepartmentSerializer

@api_view(['GET'])
def api_root(requst, format=None):
  return Response({
        'departments': reverse('departments', request=request, format=format)
    })

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    http_method_names = ['get', 'post', 'put']

    filter_backends = (filters.SearchFilter, )
    search_fields = ('department_name', 'budget')

    def get_queryset(self):
        query_set = Department.objects.all()

        keyword = self.request.query_params.get('_filter')
        if keyword == 'budget':
            keyword = keyword.lower()

            keyword = self.request.query_params.get('_gt')
            if keyword is not None:
                keyword = keyword.lower()
                query_set = query_set.filter(budget__gte=keyword)

        return query_set
