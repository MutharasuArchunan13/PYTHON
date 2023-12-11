# In python range() function used for make series of numbers
squares = []
for num in range(1,20):# exclude the last range value
    squares.append(num ** 2)

print(squares)

numbers =list(range(1,20,2))#odd numbers
print(numbers)
squar =[value**2 for value in range(1,10)]
print(squar)