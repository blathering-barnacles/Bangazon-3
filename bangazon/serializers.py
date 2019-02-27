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
    employees = Employee.objects.all()
    class Meta:
        model = Department
        fields = ('id', 'url', 'name', 'budget', 'deletedOn')


<<<<<<< HEAD
=======
class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    def __init__(self, *args, **kwargs):
        super(DepartmentSerializer, self).__init__(*args, **kwargs)
        print("ARGS: ", args)
        print("KWARGS", kwargs)
        request = kwargs['context']['request']
        print("REQUEST: ", request.query_params)
        include = request.query_params.get('_include')
        print("INCLUDE: ", include)

        if include:
            if 'employees' in include:
                self.fields['employees'] = EmployeeSerializer(many=True, source='employees.all', read_only=True)

    class Meta:
        model = Department
        fields = ('url', 'name', 'budget')

class ComputerEmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ComputerEmployee
        fields = ('__all__')

>>>>>>> master
class ComputerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Computer
        # need to add back in 'employees' into the fields once i have access to the employee resource
        fields = ('make', 'purchaseDate', 'decommissionDate', 'deletedOn', 'url', 'employees')

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    computer = ComputerSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = ('id', 'url', 'firstName', 'lastName', 'department', 'startDate', 'isSupervisor', 'deletedOn', 'computer')

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Employee
        fields = ('id', 'firstName', 'lastName', 'startDate', 'isSupervisor', 'deletedOn', 'url')

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

    fields = ('firstName', 'lastName', 'email', 'address', 'phone', 'deletedOn', 'url')


class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ProductType
        fields = ('id', 'name', 'deletedOn', 'url')


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

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    product = ProductSerializer(many=True, source='product.all', read_only=True)
    

    def __init__(self,*args,**kwargs):
        '''
        This function allows users to add a '?_include=customers' to the end of the URL in the browseable API and the buyer details will then display.
        '''

        super(OrderSerializer, self).__init__(*args, **kwargs)
        request = kwargs['context']['request']
        include = request.query_params.get("_include", None)
        if include:
            if "customers" in include:
                self.fields["buyer"] = CustomerOrderSerializer(read_only=True,)
                print("look here", request)

    class Meta:
        model = Order
        fields = ('id', 'paymentType', 'product', 'deletedOn', 'url', 'buyer')
class ProductOrderSerializer(serializers.HyperlinkedModelSerializer):
    product = ProductSerializer(read_only=True)


    class Meta:
        model = ProductOrder
        fields = ('order_id', 'product', 'deletedOn')

