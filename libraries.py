import random

alphabets=['a','e','i','o','u']

index = random.choice(alphabets)
user_input=input('Enter your guess anyone vowel')
if index == user_input:
 print('hey goog job dude ')
else:
 print('Better luck sometime')


#import some more libraries
import datetime
print('today dateTime: ',datetime.date.today(),' :',datetime.datetime.now().time())

import calendar
print(calendar.isleap(2001))

import os
print(os.getcwd(),os.__file__)