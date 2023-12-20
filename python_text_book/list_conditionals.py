usernames = ["admin","arasu","muthu","pandi","tamil"]
for username in usernames:
    if username.lower() == "admin":
        print("Welcome back admin. what we can do for you ?")
    else:
        print(f"welcome to our page {username}")

# check the username availability
current_users =["Arom","arunKumar","mutharasu","pandi","Yuvaraj","Raja"]
new_users = ["Arunkumar","maewe","otis","Ruby","Adam","PANDI"]
# new_user doesn't appear current user list
for user in new_users:
    if user.lower() in [current_user.lower() for current_user in current_users]:
        print(f"Try different username instead of {user}.")
    else:
        print(f"Username {user} is available")

#ordinal numbers
ordinal_list =[value for value in range(1,10)]
print("ordinal values:")
for ordinal in ordinal_list:
    if ordinal ==1:
        ordinal_value ="st"
    elif ordinal == 2:
        ordinal_value ="nd"
    elif ordinal == 3:
        ordinal_value = "rd"
    else:
        ordinal_value = "th"
    
    print(f"{ordinal}{ordinal_value}")
        