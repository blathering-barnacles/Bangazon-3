from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.shortcuts import get_object_or_404
from django.db.models import Q

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
        # print("SELF: ", )
        keyword = self.request.query_params.get('active', None)
        customer_query_set = Customer.objects.all()
        print("CUSTOMER QUERY: ", customer_query_set.values())
        order_query_set = Order.objects.all()

        if keyword == "false":
            # customerList = []
            notCustomerList = []
            idList = []

            # notCustomer = Customer.objects.

            for order in order_query_set:
                buyer_id = order.buyer_id
                # print("BUYER ID: ", buyer_id)
                # customer = customer_query_set.filter(id=buyer_id)
                customer = Customer.objects.all().exclude(id=buyer_id).get(id=9)
                print("CUSTOMER: ", customer)
                # customerList.append(customer)
                customerList = [customer]

            # for customer in customerList:
            #     customer_id = customer.id
            #     idList.append(customer_id)
            #     print("CUSTOMER ID: ", customer_id)
            #     # notCustomers = Customer.objects.filter(~Q(id = customer_id))
            #     notCustomers = Customer.objects.exclude(id=customer_id)
            #     print("NOT CUSTOMERS: ", notCustomers, "END OF LIST")
            #     notCustomerList.append(notCustomers)

            # print("CUSTOMER LIST: ", customerList, "END OF LIST")
            # print("NOT CUSTOMER LIST: ", notCustomerList, "END OF LIST")
            return customerList


# THIS ONE IS WORKING
        if keyword is not None:
            customerList = []


            for order in order_query_set:
                buyer_id = order.buyer_id
                # print("BUYER ID: ", buyer_id)
                # customer = customer_query_set.filter(id=buyer_id)
                customer = Customer.objects.get(id=buyer_id)
                customerList.append(customer)



            # print("CUSTOMER LIST: ", customerList)
            return customerList


        return customer_query_set
