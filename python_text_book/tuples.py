"""
TUPLES : previously i know java in java the string concept is there and commanly they say string is immutable(but use alternatives it's possible),
in python also that same concept is ther but here it's called tuples and use paranthesis instead of []
"""

names = ('Muthu','phoenix','arasu','pandi')
print(names[2])
"""once i try this i get error
   names[1]='kumar'  o/p:    names[1]='kumar'
   TypeError: 'tuple' object does not support item assignment """
# if you want to change the value to create the new tuple
restarant_menu = ('kadai','chicken','mutton','fish','veg')
print(f'Restarant menu: {restarant_menu}')
#restarant_menu[1]="crabs"  #but we got the error because tuples are immutable
# so if you want to add new idem to create new tuple
restarant_revised_menu = ('kadai','crabs','chicken','mutton','fish','veg')
print(f"Restarant revised menu: {restarant_revised_menu}") 

    