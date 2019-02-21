from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import filters
from bangazon.models import PaymentType
from bangazon.serializers import PaymentTypeSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'paymenttypes': reverse('paymenttypes', request=request, format=format),
    })

class PaymentTypeViewSet(viewsets.ModelViewSet):
    """
    Summary:
        This viewset displays a list of the Payment Types found in the database. Click on the URL of a single Payment Type to view the details  OR have the ability to delete a single instance.
    Author:
        Richard Lancaster

    """
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer