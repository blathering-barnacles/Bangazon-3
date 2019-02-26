from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Customer(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    deletedOn = models.DateField(default=None, null=True)

    def __str__(self):
        return f'{self.lastName}, {self.firstName}'

class ProductType(models.Model):
    name = models.CharField(max_length=255)
    deletedOn = models.DateField(default=None, null=True)
    # converts category choices to readable names
    def __str__(self):
      return f'{self.name}'

class Product(models.Model):
    seller = models.ForeignKey(Customer,on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    quantity = models.IntegerField()
    productType = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    dateAdded = models.DateField(default=None)
    deletedOn = models.DateField(default=None, null=True)

class PaymentType(models.Model):
    name = models.CharField(max_length=30)
    cardNum = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    deletedOn = models.DateField(default=None, null=True)

    def __str__(self):
        return f'{self.name}'

class Order(models.Model):
    buyer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    paymentType = models.ForeignKey(PaymentType, null=True, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, blank=True, through='ProductOrder')
    deletedOn = models.DateField(default=None, null=True)

class ProductOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    deletedOn = models.DateField(default=None, null=True)

class Computer(models.Model):
    '''
    description: This class creates a computer and its properties.
    author: Alfonso Miranda.
    method: there is a string method that just returns the make.
    properties:
      make = The make will contain the name of the brand of the computer.
      purchaseDate = This property contains the purchase date in string form.
      decomissionDate = This property contains the dicomission date in string form.
      employees = This property contains the many to many relationship with the computer/employee model.
    '''
    make = models.CharField(max_length=20)
    purchaseDate = models.DateField()
    decommissionDate = models.DateField(default=None, null=True)
    employees = models.ManyToManyField("Employee", through='ComputerEmployee')
    deletedOn = models.DateField(default=None, null=True)


    def __str__(self):
        ''' purpose: This method just returns the make. arguments: self '''
        return self.make

class ComputerEmployee(models.Model):
    """
    Creates the join table for the many to many relationship between computers and employees
    Author: J.Barnett
    methods: none
    """

    employee = models.ForeignKey("Employee", on_delete=models.CASCADE)
    computer = models.ForeignKey("Computer", on_delete=models.CASCADE)
    deletedOn = models.DateField(default=None, null=True)


class Department(models.Model):
    """

    Summary:
        This class creates the Department table

    Author:
        Dillon Williams

    methods:
        __str__: computes the “informal” or nicely printable string representation of an object. The return value must be a string object.

    """

    name = models.CharField(max_length=100)
    budget = models.IntegerField()
    deletedOn = models.DateField(default=None, null=True)


    """

    Purpose:
        converts data to string,
    Arguments:
        self: The first argument of every class method, including init, is always a reference to the current instance of the class. By convention, this argument is always named 'self'.

    """

    def __str__(self):
        return self.name

class Employee(models.Model):
    """

    Summary:
        This class creates the Employee table

    Author:
        Dillon Williams

    methods:
        __str__: computes the “informal” or nicely printable string representation of an object. The return value must be a string object.

    """

    department = models.ForeignKey("Department", on_delete=models.CASCADE, related_name='employees')
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    startDate = models.DateField()
    isSupervisor = models.BooleanField()
    deletedOn = models.DateField(default=None, null=True)


    def __str__(self):
        """

    Purpose:
        converts data to string,
    Arguments:
        self: The first argument of every class method, including init, is always a reference to the current instance of the class. By convention, this argument is always named 'self'.

        """
        return self.firstName, self.lastName

class EmployeeTrainingProgram(models.Model):
    """
    A model that defines a many-to-many relationship between our Employee and Training Program models and will create a table in our database
    Author: S.W., R.L.
    methods: null
    """
    # _safedelete_policy = HARD_DELETE_NOCASCADE
    employee = models.ForeignKey("Employee", on_delete=models.CASCADE)
    trainingProgram = models.ForeignKey("TrainingProgram", on_delete=models.CASCADE)
    deletedOn = models.DateField(default=None, null=True)



class TrainingProgram(models.Model):
    """
    A model that defines a Training Program and will create a table in our database with the same name
    Author: S.W., R.L.
    methods: __str__
    """

    # _safedelete_policy = HARD_DELETE_NOCASCADE
    name = models.CharField(max_length=35)
    startDate = models.DateField()
    endDate = models.DateField()
    maxAttendees = models.IntegerField()
    employee = models.ManyToManyField("Employee", through='EmployeeTrainingProgram')
    deletedOn = models.DateField(default=None, null=True)


    def __str__(self):
        ''' returns a string representation of the model '''
        return self.name

