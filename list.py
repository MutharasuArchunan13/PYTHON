names = ['arasu','muthu','kumar','pandi']

print(names)

#To acccess based on index

print(names[0])

print(names[3])   # or
print(names[-1])
#if you want access the last index use -1

#To slice the values
print(names[1:3])

#To add the values in the list
names.append('ajay')
print(names)
new_name=names[2:]
#names.append(new_name)
print(names)
#but if you want all values in the same list
names.extend(new_name)
print(names)

#insert the value in particular index
names.insert(0,'tamil')
print(names)

#To remove
names.remove('kumar') #if you want remove two 'kumar use loop
print(names)
names.pop()
print(names)

#Sorting
names.sort()
print(names)
#reverse order
names.sort(reverse=True)
print(names)

#Instead of sorted()
new_names=sorted(names)
print(new_names)

print(min(names))
print(max(names))

#finding value with index
print(names.index('tamil'))

#working with values using loop
for name in names:
    print(name)

#with index
for index,name in enumerate(names):
    print(index,name)

#specify the staring index
for index,name in enumerate(names,start=4):
    print(index,name)

#join and split
new_names=' , '.join(names)
print(new_names)

#split
updated_names=new_names.split(' , ')
print(updated_names)