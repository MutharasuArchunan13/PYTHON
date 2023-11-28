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


