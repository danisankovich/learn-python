# General object oriented programming stuff (double check)
# object: ex. a specific car can represent an object: (with properties make, model, year, registration number, owner)
# Car is a class. the car is an object of the Car class

#class is a prototype of object. Method is a function defined within the class,which can be called using the specific class or an object of that class

#Instance: an object is a specific instance of a class.

#Instantiation: creation of instance of a specific class.

#=================================================================
#=================================================================
#=================================================================

#Creating a Class
##class Car:
##    "Name of the class is Car" #just documentation/explanation
##    def __init__(self, make, model, year): #self is reference to instance of this class
##        self.make = make # the new object will be instantiated with the following paramters/properties
##        self.model = model
##        self.year = year
##        print("instance ofject of the class is created") #just confirmation of creation
##
##    def displayParameters(self):
##        print "Make: ", self.make
##        print "Model: ", self.model
##        print "Year: ", self.year
##        print


### Creating instnace objects for a class
### Object_Name = Class_Name(parameters) : this calls the init method
##
##my_car = Car("Saturn", "Vue", "2007")
##
### accessing members/properties of an object
##
##his_car = Car("a", "b", 2016)
##print "make: ", his_car.make
# his_car.displayParameters()

#=================================================================
#=================================================================
#=================================================================

# class variables
#class variables are shaped by all instances of class and defined outside of all methods for the class
# ClassName.Class_Variable_Name

class Car:
    "Name of the class is Car" #just documentation/explanation
    totalNumber = 0 ## this is a class variable. It will increase by one whenever a new object is made from this class
    def __init__(self, make, model, year): #self is reference to instance of this class
        Car.totalNumber += 1
        self.make = make # the new object will be instantiated with the following paramters/properties
        self.model = model
        self.year = year
        print("instance ofject of the class is created") #just confirmation of creation

    def displayParameters(self):
        print "Make: ", self.make
        print "Model: ", self.model
        print "Year: ", self.year
        print

his_car = Car("a", "b", 2016)
your_car = Car("c", "d", 2010)
my_car = Car("e", "f", 2012)

his_car.displayParameters()
your_car.displayParameters()
my_car.displayParameters()
print Car.totalNumber
