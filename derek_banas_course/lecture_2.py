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


# import random

# rand_num = random.randrange(1, 61)
# i = 1
# while (i != rand_num):
#     i = i + 1

# print("the random value is : ", rand_num)

# i = 1

# while i <= 20:
#     if (i % 2) == 0:
#         i += 1
#         continue
    
#     if i == 15:
#         break
    
#     print("Odd : ", i)
    
#     i += 1  



""" How tall is the tree : 5

 print out the tree

    #
    ###
    ####

 use 1 while loop and 3 for loops iteration
 4 spaces and 1 hash
 3 spaces and 3 hashes
 2 spaces and 5 hashes
 1 space and  7 spaces
 0 space and 9 hashes

 Need to Do
 decrement spaces by 1 each time  through the loop
 increment hashes by 2 each time through
 save spaces to the  stump by calculating  tree height - 1
 decrement from tree height untill equals 0
 print spaces and then hashes for each row
 print stump spaces  and then 1 hash

"""
# Get the number of rows for the tree


# convert into an integer


# get the starting spaces for the  top of the tree

# there is one hash to start that will be incremented

# save the stump till later

# make sure  the right number are printed

# print spaces 
#end=''
