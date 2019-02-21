from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework import filters

from bangazon.models import Computer
from bangazon.serializers import ComputerSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'computers': reverse('computers', request=request, format=format),
    })

class ComputerViewSet(viewsets.ModelViewSet):
    """
    Summary:
        This viewset displays a list of the Computers found in the database. Click on the URL of a single computer to view the computer details  OR have the ability to delete the computer instance.
    Author: 
        Dillon Williams

    """
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer