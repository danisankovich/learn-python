class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color
    def show_info(self):
        print("last Name - " + self.last_name)
        print("Eye Color - " + self.eye_color)

class Child(Parent):#Child class inherits everything from Parent class
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child constructor called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys
    def show_info(self):
        print("last Name - " + self.last_name)
        print("Eye Color - " + self.eye_color)
        print("number of toys - " + str(self.number_of_toys))

billy_cyrus = Parent("Cyrus", "blue")
#billy_cyrus.show_info()
miley_cyrus = Child("Cyrus", "Blue", 5)
miley_cyrus.show_info() # you can do this without
# explicitly defining it in Child because child inherits from parent.
# if you do redefine it though, it will do Method Override
