student = {'name': 'joshua', 'age': 13}
print(student.get('name'))
student.update({'name': 'alana', 'age': 12})
print(student)
print(len(student))

for key, value in student.items():
    print(key, value)