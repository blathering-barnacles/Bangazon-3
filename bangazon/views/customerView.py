from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.shortcuts import get_object_or_404

from rest_framework import filters

from bangazon.models import Customer, Order
from bangazon.serializers import ProductSerializer, CustomerSerializer


@api_view(['GET'])
def api_root(requst, format=None):
  return Response({
        'customers': reverse('customers', request=request, format=format)
    })

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
#   print("QUERY: ", queryset)
    serializer_class = CustomerSerializer
    # filter_backends = (filters.SearchFilter, )
    # search_fields = ('id', 'firstName', 'lastName', 'email', 'address', 'phone', 'deletedOn', 'url')


    def get_queryset(self):

        keyword = self.request.query_params.get('active', None)
        customer_query_set = Customer.objects.all()
        print("CUSTOMER QUERY: ", customer_query_set)
        order_query_set = Order.objects.all()
        # print("ORDER QUERY: ", order_query_set)
        # activeCustomers = []


        if keyword is not None:
            customerList = []
            # woop = (customerList)

            # activeCustomers = []

            for order in order_query_set:
                # print("order buyer id: ", order.buyer_id)
                buyer_id = order.buyer_id
                customer = customer_query_set.filter(pk=buyer_id)
                # print("CUSTOMER: ", customer)
                customerList.append((customer))



                # customerList = { 'customers': customer}
                # print(customerList)
                # activeCustomers.append(customerList)

            # for person in customerList:
                # print(customerList)
                # print("person: ", person)
                # for name in person:
                    # print(name)
            # print("CONTEXT: ", context)
            print("CUSTOMER LIST: ", customerList)
            # print("woop", woop)
            return customer


        return customer_query_set


    # class TrainingProgramViewSet(viewsets.ModelViewSet):
    # queryset = TrainingProgram.objects.all()
    # serializer_class = TrainingProgramSerializer

    # filter_backends = (filters.SearchFilter, )
    # search_fields = ('id', 'name', 'startDate', 'endDate', 'maxAttendees', 'deletedOn', 'url')
    # # search_fields = ('id', 'firstName', 'lastName')

    # def get_queryset(self):
    #     print("TIME: ", str(datetime.datetime.now())[0:10])
    #     # today = str(datetime.datetime.now())[0:10]
    #     today = datetime.datetime.now()
    #     query_set = TrainingProgram.objects.all()
    #     # print("query", query_set[0])
    #     keyword = self.request.query_params.get('completed', None)

    #     if keyword == "false":
    #         query_set = query_set.filter(startDate__gte=today)
    #     elif keyword == "true":
    #         query_set = query_set.filter(endDate__lte=today)
    #     elif keyword is not None:
    #         query_set = query_set.filter(startDate__gte=today)

    #     return query_set

