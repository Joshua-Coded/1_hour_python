import random
import datetime
import calendar

from my_module import find_index

courses = ['math', 'css', 'c++', 'python', 'java']
index = find_index(courses, 'css')
print(index)

# getting random course
random_course = random.choice(courses)
print(random_course)

todays = datetime.date.today()
print(todays)