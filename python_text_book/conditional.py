# In programing we want to check conditions to use conditional statements 

num_1 = 25
num_2 = 20
if num_1 > num_2:
    print(f'{num_1} grater than {num_2}.') 

# if you want check two more conditional all conditions are satisfied then only execute our logic
num_3 =30
if (num_1 >num_2) and (num_3 >num_1):
    print(f"{num_3} is greater than {num_1} and {num_2}")
else:
    print(f'{num_3} isn\'t bigger one.' )

#if you want check the particular value in the list or not
user_names =['fabilo','aron','pangu','azhagi']
new_user ='aron'
if new_user in user_names:
    print(f'Sorry.. use different username')
else:
    print(f'username avilable you can continue.....')


# check the value not in the list
if 'kumar' not in user_names:
    print(f'username is available you can continue....')
else: 
    print(f'Sorry try different username')