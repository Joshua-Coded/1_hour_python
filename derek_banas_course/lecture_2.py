# # # # learn to program in python with derek banas
# # # # write a program that prints odds from range of 1-21
# # # #solution
# # # # use for loop
# # # for i in range(1, 21):

# # # # use modulos to check that the result is not equal to zero
# # #     if ((i % 2) != 0):
# # # # print the odds
# # #         print("i = ",  + i)

# # # working with foating numbers
# # your_float = input("Enter a float value: ")
# # your_float = float(your_float)
# # print("Rounded to 2 decimal : {:.2f}".format(your_float))


# # have the users enter their investment amounts and their interest
# # each year their investment will increase by their investment + their investment * interest
# # print out the earnings after a 10 year period

# #solution

# #Ask for the money invested + the interest interest

# money = input("How much to invest: ")
# interest_rate = input("Interest rate: ")

# #convert the value to a float

# money = float(money)

# #convert value to a float and round  the percentage rate by 2 digits
# interest_rate = float(interest_rate) * .01
# # cycle through 10 years using a for loop and range from 0 to 9
# for i in range(10):
#     money = money + (money * interest_rate)

# # output the  result
# print("Investment after 10 years: {:.2f}".format(money))


