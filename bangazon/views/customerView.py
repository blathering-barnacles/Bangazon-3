from django.db.models import Q
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import filters

from bangazon.models import Customer
from bangazon.models import Order
from bangazon.serializers import ProductSerializer
from bangazon.serializers import CustomerSerializer


@api_view(['GET'])
def api_root(requst, format=None):
  return Response({
        'customers': reverse('customers', request=request, format=format)
    })

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get_queryset(self):
        keyword = self.request.query_params.get('active', None)
        customer_query_set = Customer.objects.all()
        print("CUSTOMER QUERY: ", customer_query_set.values())
        order_query_set = Order.objects.all()

        if keyword == "false":
            notCustomer = Customer.objects.filter(active=False)

            return notCustomer

        elif keyword == "true":
            customerList = []


            for order in order_query_set:
                buyer_id = order.buyer_id
                customer = Customer.objects.get(id=buyer_id)
                customerList.append(customer)

            return customerList

        elif keyword is not None:
            customerList = []


            for order in order_query_set:
                buyer_id = order.buyer_id
                customer = Customer.objects.get(id=buyer_id)
                customerList.append(customer)

            return customerList


        return customer_query_set
