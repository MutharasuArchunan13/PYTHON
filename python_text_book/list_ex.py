#create a list of friend for inviting dinner
friends =['arasu','pandi','muthu','fazil','kumar']
# print invite message for each friends in a list 
print('welcome to our home :'+ friends[0])
print('welcome to our home :'+ friends[1])
print('welcome to our home :'+ friends[2])
print('welcome to our home :'+ friends[3])
print('welcome to our home :'+ friends[4])
# next we prepare a list for dinner so invite all for dinner but arasu can't make dinner so remove the arasu from the list
friends.remove('muthu')
dinner_friends = friends 
# invite new friend then add that friend on muthu place
dinner_friends.insert(2,'yal')
print(dinner_friends)
print('welcome to our home :'+ dinner_friends[2])
#now we have big dining table so invie more peoples so use insert() insert two friends one is starting and another one is middle 
dinner_friends.insert(0,'arun') #starting
middle = int(len(dinner_friends) /2)
dinner_friends.insert(middle,'john')
# add member end of the list using append
dinner_friends.append('mutharasu')
print(dinner_friends)
print(len(dinner_friends))
#now the table is occupied in another guest now only two seats are avilable so say sorry invite apart from those two peoples 
print('i am realy feel bad that situatiion'+dinner_friends.pop())
print('i am realy feel bad that situatiion'+dinner_friends.pop())
print('i am realy feel bad that situatiion'+dinner_friends.pop())
print('i am realy feel bad that situatiion'+dinner_friends.pop())
print('i am realy feel bad that situatiion'+dinner_friends.pop())
print('i am realy feel bad that situatiion'+dinner_friends.pop())

#rest of two people invite to seat the dinner
print('please take your seat  :'+dinner_friends[0])
print('please take your seat  :'+dinner_friends[1])

del dinner_friends[1]
del dinner_friends[0]
print(dinner_friends)

#excercise 2
# create list of fvrt places would you like to go non-alphabetical order
places = ['thanjavur','acra','karuppur','coimbatore','ooty','pondi','kanyakumari']
print(places)
# use sorted method because don't affect the orginal  list
sorted_places = sorted(places)
print(sorted_places)
# print the original list 
print(places)
#reverse alphabeticla order
reverse_places = sorted(places,reverse=True)
print(reverse_places)
# original list
print(places)

places.reverse()
print("reverse order :",places)
places.reverse()
print('once again reverse order:',places)

# use sort() to print the values in sorted order
places.sort()
print('after use sort method:',places)

# use sort() to reverse order
places.sort(reverse=True)
print('print reverse albhabetical :',places)

# make a index errror 
# print('length of the list: ',len(places))
# print(places[7])

# for loop with list
gang =['saravana','mahendra','arasu','uthaya','mari','rajesh','muhesh','karthi']
for guy in gang:
    print(guy.title()," is a good person but don't show of others.")
    print('That is the good thing. \n')
print('All guys are made the gang.')

# print gang name with place name
print(len(gang),len(places))
combined_name_place = list(zip(gang,places))
for gang,places in combined_name_place:
    print(f'{gang} wants to go {places}')