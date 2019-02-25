from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework import filters

from bangazon.models import Order
from bangazon.models import PaymentType
from bangazon.models import Customer
from bangazon.serializers import OrderSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'orders': reverse('orders', request=request, format=format),
    })

class OrderViewSet(viewsets.ModelViewSet):
    """
    Summary:
        This viewset displays a list of the Orders found in the database. Click on the URL of a single order to view the order details OR have the ability to delete the order instance.
    Author: 
        Dillon Williams

    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # filter_backends = (filters.SearchFilter,)
    # search_fields = ('paymentType_id')

    def get_queryset(self):
        query_set = Order.objects.all()
        keyword = self.request.query_params.get('completed', None)
        if keyword == 'true':
            query_set = query_set.exclude(paymentType_id__isnull=True)
        elif keyword == 'false':
            query_set = query_set.exclude(paymentType_id__isnull=False)
        return query_set
