#there are two primitive loops there for and while loop
'''
for loop used for we know the process takes how many times use for-loop
we want the process work until our contion is satisfied
'''

for value in range(10):
    print(value) 
print('----------------------------------------------------------------------------------------------------------------------------')
for i in range(3,20):
    if i ==5:
        break
    print(i)

print('-------------------------------------------------------------------------------------------------------------------------------------')
for i in range (10):
    if i ==6:
        continue
    print(i)

value=20
while value > 0:
    print(value)
    value-=1



for i in range(1, 6):
    for j in range(i):
        print("*",end="")
    
    print()

