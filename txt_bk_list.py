# here we create the list --> collection of items in order

brands = ['hp','lenova','acer','apple','ms','moto',]
print(brands)
#access particular index
print(brands[3])
#add elements
brands.append('samsung')
print(brands)

#access last elment in  the list
print(brands[-1])
# we can also insert the value in particular index using insert method
brands.insert(0,'MOTO')
print(brands)

# if you want insert maybe if you don't want also remove
del brands[3]
print("after del:",brands)
# the above example we can't access after the deletion may if you want access use pop method, it removes end of the element in the list
removed_val = brands.pop(2)#we can also aceess the particcular element also

print("after pop:",brands)
print('removed_value',removed_val)
# sometimes we don't know about the value position only know  the value only now the remove entire the playground
brands.remove('ms')
print("after removed item and list :"+str(brands))

#excercise
guests =['joe','king ', 'jose','crimson','selva']
while  guests.__len__() >=0:
  print('hi '+guests.pop()+' welcome to our home and lets start!')
