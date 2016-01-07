# if (condition): task_if
# if condition: task_if
# number = input()
# if number == 2: print("The number is two")
# elif number == 10: print("That's odd, it's ten")
# else: print("The number is not 2 or 10, the number is " + str(number))

# if, else (if all other conditions are false), elif

# you can do this with inentations too.

number = input()
if number == 2 | 3:
    print("The number is two or 3")
elif number == 10:
    print("That's odd, it's ten")
else:
    print("The number is not 2, 3, or 10, the number is " + str(number))
