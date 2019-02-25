from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework import filters

from bangazon.models import Order
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