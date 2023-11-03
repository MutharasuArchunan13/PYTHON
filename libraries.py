import random

alphabets=['a','e','i','o','u']

index = random.choice(alphabets)
user_input=input('Enter your guess anyone vowel')
if index == user_input:
 print('hey goog job dude ')
else:
 print('Better luck sometime')