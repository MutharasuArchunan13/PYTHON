message = 'Hello World\'s '

print(message)

print(len(message))

print(message[0:5])
print(message[:5])

print(message.upper())

print(message[5:])

print("find: ",message.find('o'))  #find is used to find the index to start the character

print('count:',message.count('o'))
message=message.replace("World's",'arasu')

print(message)


#concat
greets= 'Hello'
name='Mutharasu'
message=greets +' '+name
print(message)

#But we can also use format() string
new_message= '{},{}.welcome'.format(greets,name)
print(new_message)

#there is another way to fstring
messages=f'{greets},{name}'+' welcome to my world'
print(messages)