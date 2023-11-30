#the collection item doesn't follow any acending or decesing order so usd predefined funtion to sort the values as you want
friends =['afrin','zen','muthu','kumar','lalith']
print(friends)
friends.sort()
print('after sorted :',friends)
 # if you want sorting reverse order sorted values
friends.sort(reverse=True)
print('in reverse order :' ,friends) 
# but now we want the value the sorted value don't affect the original list use for sorted()
friends =['afrin','zen','muthu','kumar','lalith']
print('Temprary sorted values :',sorted(friends))#it doesn't affect orignal values in the list
print('original values :',friends)
# To reverse  the order on original values
friends.reverse()
print('reverse order in original values :',friends) 
# find the length
print('length of the list',len(friends))

