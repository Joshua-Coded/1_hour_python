#ask the user to input their name and assign it to a variable named name

# name = input('What is your name ')

# print out their name followed by the name they entered.
# print('Hello ', name)

#-------------------------------------------------------------------------
# Ask the user to input 2 values and store them in variables num1 and num2
 
num1, num2 = input('Enter  2 numbers: ').split()
 # convert the strings the user entered into regular numbers Integer
num1 = int(num1)
num2 = int(num2)
 
 # add the values entered and store in sum  
sum = num1 + num2
 # subtract the values entered and store in diff
diff = num1 - num2
# multiply the values entered and store in prod
mul = num1 * num2
# divide the values entered and store in quotient
div = num1 / num2
# use modulos on the value to find the remainder
mod = num1 % num2
# print the result on the screen for the user.
print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, diff))
print("{} * {} = {}".format(num1, num2, mul))
print("{} / {} = {}".format(num1, num2, div))
print("{} % {} = {}".format(num1, num2, mod))