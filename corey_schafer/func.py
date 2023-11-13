# # def hello_func():
# #     print("Hello function thank you for been one")

# # hello_func()

# # #DRY concept

# # def hello_me(greeting):
# #     return '{} function'.format(greeting)

# # print(hello_me("hello"))

# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)
    
# courses = ['math', 'Physics']
# info = {'name': 'joshua', 'age': 12}

# student_info(*courses, **info)


month_days = [0,31,28,31,30,31,30,31,30,31,30,]

def is_leap(year):
    # return true if year is leap
    return year % 4 == 0 and (year % 100 != 0 or year % 400 != 0)
