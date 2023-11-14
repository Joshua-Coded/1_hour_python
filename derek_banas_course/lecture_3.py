# # # working with python string

# # while True:
    
# #     try:
# #         number = int(input("Enter a number : "))
# #         break
    
# #     except ValueError:
# #         print("You didn't enter a number")
        
# #     except:
# #         print("An unknown error occurred")
# # print(number)


# # problem : implementating do while loop
# # this should be a guessing game between 1  and 10 : 1
# # 

# # secret_number = 7

# # while True:
# #     guess = int(input("Guess the secret number between 1 and 10: "))
    
# #     if guess == secret_number:
# #         print("You guessed it right")
# #         break



# sam_string = "This is the best developer on the planet."

# print("Lenght: ", len(sam_string))

# print(sam_string[0:4])


#Enter a string to hide in uppercase

# secret message : 

# original  message :


# hints

# input  "Enter a string to hide in uppercase"
norm_string = input("Enter a string to hide in uppercase: ")

secret_string = " "
# cycle through each character  in the string
for char in norm_string:
#store the character code in a new string
    secret_string += str(ord(char) - 23)
# print  "secret message"
print("secret message", secret_string)
# cycle through each character code 2 time by incrementing by 2  each time
norm_string = ""

for i in range(0, len(secret_string)-1, 2):
    
# get the 1st and 2nd  for the 2  digit number
    char_code  = secret_string[i] + secret_string[i+1]

    norm_string += chr(int(char_code) + 23)
    
print("Original secret string: ", norm_string)
