#[start:end:step]   start--> start_index(inclusive),end(not-inclusive),step(index moving steps)

numbers=[1,2,3,4,5,6,7,8,9]
#index   0 1 2 3 4 5 6 7 8
#reverse -9-8-7-6-5-4-3-2-1

print (numbers[1:6])
print(numbers[::-1])
print(numbers[::-3])
print(numbers[:-1:2])

names=['muthu','pandi','arasu','mari','uthaya']
print(names[2::-1])
print(names[::-1])