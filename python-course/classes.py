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
class Car:
    "Name of the class is Car" #just documentation/explanation
    def __init__(self, make, model, year): #self is reference to instance of this class
        self.make = make # the new object will be instantiated with the following paramters/properties
        self.model = model
        self.year = year
        print("instance ofject of the class is created") #just confirmation of creation

    def displayParameters(self):
        print("Make: ", self.make)
        print("Model: ", self.model)
        print("Year: ", self.year)
        print()
