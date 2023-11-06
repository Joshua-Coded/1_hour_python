#ask the user to input their name and assign it to a variable named name

# name = input('What is your name ')

# print out their name followed by the name they entered.
# print('Hello ', name)

#-------------------------------------------------------------------------
# Ask the user to input 2 values and store them in variables num1 and num2
 
# num1, num2 = input('Enter  2 numbers: ').split()
 # convert the strings the user entered into regular numbers Integer
# num1 = int(num1)
# num2 = int(num2)
 
 # add the values entered and store in sum  
# sum = num1 + num2
 # subtract the values entered and store in diff
# diff = num1 - num2
# multiply the values entered and store in prod
# mul = num1 * num2
# divide the values entered and store in quotient
# div = num1 / num2
# use modulos on the value to find the remainder
# mod = num1 % num2
# print the result on the screen for the user.
# print("{} + {} = {}".format(num1, num2, sum))
# print("{} - {} = {}".format(num1, num2, diff))
# print("{} * {} = {}".format(num1, num2, mul))
# print("{} / {} = {}".format(num1, num2, div))
# print("{} % {} = {}".format(num1, num2, mod))

# ------------------------------------------------------------------
# problem : receive miles and convert to kilometer
# kilometer = miles * 1.60934
# enter miles in 5 '
# 5 miles equals 8.04 kilometers

# solution:

#ask the user to input miles and assign it to a mile variable
# miles = input('Enter miles ')

# convert from string to integer
# miles = int(miles)

# perform calculation by multiplying 1.680943 times miles
# kilometers = miles * 1.60943

# print results using format()
# print("{} miles equals {} kilometers".format(miles, kilometers))



# enter calculation: 5 * 6
# 5 * 6 = 30

# store the user input of 2 numbers and the operator
# num1, operator, num2 = input('Enter Calculation').split()

# convert the strings into integers
# num1 = int(num1)
# num2 = int(num2)

# if  + then we need to provide output based on addition

# if operator == "+":
#     print("{} + {} = {}".format(num1, num2, num1 + num2))
# elif operator == "-":
#     print("{} - {} = {}".format(num1, num2, num1 - num2))
# elif operator == "*":
#     print("{} * {} = {}".format(num1, num2, num1 * num2))
# elif operator == "/":
#     print("{} / {} = {}".format(num1, num2, num1 / num2))
# else:
#     print("use either + - * / next time")


# ------------------------- 
# We will provide different output based on age
# 1 - 18 -> important
# 21 - 50 -> important
# all others -> not important

# receive age and store in age
age = eval(input("Enter age: "))

# if age is both greater than or equals to 1 and less than or equal to 18 important
if (age >= 18) and (age <= 18):
    print("Important Birthday")
# and : if both condition are true it returns true
elif (age == 21 ) or (age == 50):
    print("Important Birthday")
    
# or : if either condition is false it returns false
elif not (age < 65):
    print("Important Birthday")
# not : covert true condition into false condition
else:
    print("sorry not Important Birthday")
