#tuples also like as list but the difference is tuples are immutable like String in java

tupel_1=('MUTHU','phoenix','arasu','abi')  #the difference to declaration is [] --->()
tuple_2=tupel_1
tupel_1[0]='Arasu Archunan'  #TypeError: 'tuple' object does not support item assignment
print(tupel_1)
print(tuple_2)