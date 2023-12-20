#To check the condition in python using if contional statements 

valuess = True
if valuess ==True:
    print(' the value is true') 

#if else statements
a=40
b=20

if a > b:
    print('a is greater than b')
elif b > a:
    print('b is greater than a')
else: 
  print("a and b is equal")  

num =0
if a and num:
    print('the variables contain values')
if a or num:
    print('one value is false other is true')
if not num:
   pass
# pass statement to avoid to get the error

#create 10 list forcodintionals

bikes = ["RX-100","RS200","classic-350","Jawa","R15"]
if "Jawa" in bikes:
    print("Jawa is in the list")
if "RS200" in bikes:
    print("RS200 is in the list")
if "R15" in bikes:
    print("R15 is in the list")
if "classic-350" in bikes:
    print("classic-350 is in the list")
if "RX-100" in bikes:
    print("RX-100 is in the list")
if "RX-100" in bikes:
    print("RX-100 is in the list")
if "HONDA" not in bikes:
    print("HONDA is not in the list")
    
# create variable alien color green,yellow,red
alien = "green"
if alien.lower() == "green":
    print("Now the player earned 5 points")
elif alien.lower() !="green":
    print("now the player earned 10 points")
else:
    print("now the player earned 15 points")

# based on age we say baby,toddler,kid,tenager,adult,elder
# age = int(input("enter your age: "))
age = 20
if age < 2:
    print(" you are the baby")
elif (age > 2) and (age < 4):
    print(" you are the toddler")
elif (age > 4) and (age <12):
    print(" you are the kid")
elif (age > 12) and (age <18):
    print("you are the teenager")
elif (age > 18) and (age < 65):
    print("yor are the adult")
else:
    print("you are the elder")

fruits = ["apple","banana","gova"]
if "apple" in fruits:
    print("apple is in the list")
if "banana" in fruits:
    print("banana is in the list")
if "gova" in fruits:
    print("gova is in the list")
    

