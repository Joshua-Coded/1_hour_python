# def hello_func():
#     print("Hello function thank you for been one")

# hello_func()

# #DRY concept

# def hello_me(greeting):
#     return '{} function'.format(greeting)

# print(hello_me("hello"))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
    
courses = ['math', 'Physics']
info = {'name': 'joshua', 'age': 12}

student_info(*courses, **info)