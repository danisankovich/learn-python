# y = input("The Meaning of Life: ");
# if y == 42:
#     print "you are correct"
# else:
#     print "EXTERMINATE"
#
name = raw_input("What is your name? ") #takes input and makes it string
age = input("How old are you, " + name + "? ") #takes input as is. if you are trying to use a string, but do not type in quotes, it will throw error
print "I see, " + name + ", you are " + str(age) + " years old."
