# Use this to take notes on the Edpuzzle video. Try each example rather than just watching it - you will get much more out of it!
#  

student = {'name': 'Parker', 'age': 15, 'courses': ['Math', 'Compsci']}

#student['phone'] = '888-8888'
#student['name'] = 'Jane'

student.update({'name': 'jane', 'age': 25, 'phone': '888-8888'})

#del student['age']

age = student.pop('age')

# print(student.get('phone', 'Not Found'))
print(student)
#print(age)
#print(len(student))
#print(student.keys())
#print(student.values())
print(student.items())

for key, value in student.items(): 
    print(key, value)


