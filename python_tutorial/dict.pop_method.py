student = {'name': 'Raj', 'age': 20, 'grade': 'A'}
value = student.pop('grade', 'Not Found')
print(value)        # Output: A
print(student)      # Output: {'name': 'Raj', 'age': 20}