from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework import filters

from bangazon.models import Department
from bangazon.models import Employee
from bangazon.serializers import DepartmentSerializer
# from bangazon.serializers import EmployeeSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    http_method_names = ['get', 'post', 'put']

    # filter_backends = (filters.SearchFilter,)
    # search_fields = ('name', 'deletedOn')

    # def get_queryset(self):
    #     query_set = Employee.objects.all()
    #     departments = Department.objects.all()
    #     keyword = self.request.query_params.get('_include', None)
    #     # if keyword == 'employees':
    # return queryset

    # def get_queryset(self):
    #     query_set = Order.objects.all()
    #     keyword = self.request.query_params.get('completed', None)
    #     if keyword == 'true':
    #         query_set = query_set.exclude(paymentType_id__isnull=True)
    #     elif keyword == 'false':
    #         query_set =query_set.exclude(paymentType_id__isnull=False)
    #     return query_set