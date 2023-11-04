#python dictionary have key: value pairs like in other languages map(java)

# key --> unique identifier
#value -->is a data
student ={'name':'Muthu','age':20,'job':'developer'}

for value in student.values():
 print(value)
 
 
for key in student:
 print(key,student.get(key))

# there one advantage to use get() because if the key isn't available it return only None not a error
# print(student['namee'])   it's show the error
print(student.get('namee'))

#  keys list
print(student.keys())
# values list
print(student.values())
#key and values
print(student.items())