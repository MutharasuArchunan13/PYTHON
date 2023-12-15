#print 1 to 20
# In list comphrehension it's possible to print the 1 to 20 using one line code 
[print(index)for index in range(1,20)]

list_for_millon=[value for value in range(1,1000000)]
# print(list_for_millon)
#use predefined function to find min(), max(),sum()
print(f'maximun value: {max(list_for_millon)} \nminimum value: {min(list_for_millon)} \nsum of values: {sum(list_for_millon)}')

# use third argument in range() to print the odd numbers
odd_numbers=[value for value in range(1,20,2)]
print(odd_numbers)

#to print multiplies of 3and  starts from 3 to 30
power_three =[value**3 for value in range(3,30)]
print(power_three)

# print power of three each number and the range(1,10)
cube =[value**3 for value in range(1,10)]
print(cube)

# Slice in list: to seperate tfrom array like range()
names_of_district = ['pudugai','thanjai','trichy','karur','kovai','tirupur']
print(names_of_district[0:3]) # include starting index and exclude ending index
print(names_of_district[:3]) # start form 0
print(names_of_district[0:]) # end with last index
print(names_of_district[:-1]) # until go last element in the list(but last element exclude)
print(names_of_district[:]) #start first to last element
#using for loop 
for value in names_of_district[0:3]:
    print(value)
