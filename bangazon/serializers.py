from rest_framework import serializers
from bangazon.models import Customer
from bangazon.models import ProductType
from bangazon.models import Product
from bangazon.models import PaymentType
from bangazon.models import ProductOrder
from bangazon.models import Order
from bangazon.models import Computer
from bangazon.models import ComputerEmployee
from bangazon.models import Department
from bangazon.models import Employee
from bangazon.models import EmployeeTrainingProgram
from bangazon.models import TrainingProgram


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Employee
        fields = ('id', 'firstName', 'lastName', 'startDate', 'isSupervisor', 'deletedOn', 'url')

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Department
        fields = ('id', 'url')
class ComputerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Computer
        # need to add back in 'employees' into the fields once i have access to the employee resource
        fields = ('make', 'purchaseDate', 'decommissionDate', 'deletedOn', 'url')
