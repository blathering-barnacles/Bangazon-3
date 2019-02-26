from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework import filters

from bangazon.models import Department
from bangazon.models import Employee
from bangazon.serializers import DepartmentSerializer
# from bangazon.serializers import EmployeeSerializer

@api_view(['GET'])
def api_root(requst, format=None):
  return Response({
        'departments': reverse('departments', request=request, format=format)
    })

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    http_method_names = ['get', 'post', 'put']

    # filter_backends = (filters.SearchFilter,)
    # search_fields = ('name', 'deletedOn')

    # def get_queryset(self):
    #     query_set = Employee.objects.all()
    #     departments = Department.objects.all()
    #     keyword1 = self.request.query_params.get('_include', None)
    #     # if keyword1 == 'employees':
    #     keyword2 = self.request.query_params.get('_filter', None)
    #     if keyword2 == 'budget':
    #         query_set = Department.objects.filter(budget__gte=300000)
    #     return queryset

    # def get_queryset(self):
    #     query_set = Order.objects.all()
    #     keyword = self.request.query_params.get('completed', None)
    #     if keyword == 'true':
    #         query_set = query_set.exclude(paymentType_id__isnull=True)
    #     elif keyword == 'false':
    #         query_set =query_set.exclude(paymentType_id__isnull=False)
    #     return query_set
    filter_backends = (filters.SearchFilter,)
    search_fields = ('budget')



# class IsOwnerFilterBackend(filters.BaseFilterBackend):
#     """
#     Filter that only allows users to see their own objects.
#     """
#     def filter_queryset(self, request, queryset, view):
#         return queryset.filter(owner=request.user)
