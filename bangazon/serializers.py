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



class DepartmentSerializer(serializers.HyperlinkedModelSerializer):

    # assignees = EmployeeSerializer(many=True, source='employee.all', read_only=True)

    class Meta:
        model = Department
        fields = ('id', 'url', 'name', 'budget', 'deletedOn')

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):

    departments = DepartmentSerializer(many=True, source='department.all', read_only=True)

    class Meta:
        model = Employee
        fields = ('id', 'firstName', 'lastName', 'startDate', 'isSupervisor', 'deletedOn', 'url', 'departments')

class ProductSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Product

    fields = ('title', 'location', 'description', 'price', 'quantity', 'dateAdded', 'deletedOn', 'productType_id', 'seller_id', 'url')

class CustomerSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Customer

    fields = ('firstName', 'lastName', 'email', 'address', 'phone', 'deletedOn', 'url')

class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ProductType
        fields = ('id', 'name', 'deletedOn', 'url')

class ComputerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Computer
        # need to add back in 'employees' into the fields once i have access to the employee resource
        fields = ('make', 'purchaseDate', 'decommissionDate', 'deletedOn', 'url')

class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PaymentType
        fields = '__all__'

class ProductOrderSerializer(serializers.HyperlinkedModelSerializer):
    product = ProductSerializer(read_only=True)


    class Meta:
        model = ProductOrder
        fields = ('order_id', 'product', 'deletedOn')
