import random
from my_module import find_index

courses = ['math', 'css', 'c++', 'python', 'java']
index = find_index(courses, 'css')
print(index)

# getting random course
random_course = random.choice(courses)
print(random_course)