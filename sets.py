#sets also contain a collection of values but not follow the insertion order
sets_1={'kumar','murugan','arasu','phoenix','phoenix'}

sets_2={'arasu','phoenix','king'}
print(sets_1)
print(sets_1.intersection(sets_2))
print(sets_1.difference(sets_2))
#we want a both list unique values
print(sets_1.union(sets_2))
#To empty creation of list,tuples,sets
''' 
  list_1=[]  or list_1=list()
  tuples_1=()  OR tuples_1=tuple()
  sets_1 = {} --> not valid  so use  sets_1=set()
'''
