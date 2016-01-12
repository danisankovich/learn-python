# number = 0
# while number <= 100:
#     print int(number), " is the current number"
#     number += 1

# beginning = 0
# end = 100
# step = 1
# for number in range(0, end + 1, step): #range means from the beginning to end, non inclusive of end
#     print int(number), " is the current number"

# list = ["book", "tape", "film", "magazine", "game"]
# for item in list: #item in list does the whole thing
#     print item, " is the current item"

# continue=== skip the remaining part of current step of loop if specifi condition is true
 # break=== leave loop if certain condition is true
 # pass=== dont dop anything if some condition is true

# number = 11
# while number >=1: #displays 10 ==> 0
#     number -=1
#     print number

# number = 11
# while number >=1: #displays 10 ==> 0, but will skip when number == 5
#     number -=1
#     if number == 5:
#         continue
#     print number

# number = 11
# while number >=1: #displays 10 ==> 0, but will terminate loop should number == 5
#     number -=1
#     if number == 5:
#         break
#     print number

# number = 11
# while number >=1: #displays 10 ==> 0, nothing extra will be done should number == 5, so it will still print everything
#     number -=1
#     if number == 5:
#         pass
#     print number

#foor loops can use break, continue, and pass as well
# beginning = 0
# end = 15
# step = 1
# for number in range(beginning, end + 1, step):
#     if number == 5:
#         break
#     print number
#
# for number in range(beginning, end + 1, step):
#     if number == 5 | 7:
#         continue
#     print number

# for number in range(beginning, end + 1, step):
#     if number == 5:
#         pass
#     print number

# while(True): #enter into an infinite loop (sort of. You can break out wiht proper input)
#     pw = raw_input("Enter Password: ")
#     if pw == "awesomepassword":
#         break
# print("Access Granted")
