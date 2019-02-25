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
        fields = ('id', 'url', 'name', 'budget', 'deletedOn')

class ProductSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Product

    fields = ('title', 'location', 'description', 'price', 'quantity', 'dateAdded', 'deletedOn', 'productType', 'seller', 'url')

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    product = ProductSerializer(many=True, read_only=True)

    class Meta:
      model = Customer

      fields = ('firstName', 'lastName', 'email', 'address', 'phone', 'product', 'deletedOn', 'url')


class CustomerOrderSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Customer
    fields = '__all__'
    

class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ProductType
        fields = ('id', 'name', 'deletedOn', 'url')

class ComputerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Computer
        # need to add back in 'employees' into the fields once i have access to the employee resource
        fields = ('make', 'purchaseDate', 'decommissionDate', 'deletedOn', 'url')

class TrainingProgramSerializer(serializers.HyperlinkedModelSerializer):
    # first_name = serializers.ReadOnlyField(source='employee.firstName')
    attendees = EmployeeSerializer(many=True, source='employee.all', read_only=True)


    class Meta:
        model = TrainingProgram
        fields = ('id', 'name', 'startDate', 'endDate', 'maxAttendees', 'deletedOn', 'url', 'attendees' )

class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PaymentType
        fields = '__all__'
