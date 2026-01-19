#validate user input exercise
#1. Username is no more than 12 caharacters
#2. Username doesn't contain spaces
#3. Username doesn't contain numbers

username = input("Enter your username : ")

if len(username)>12:
    print("Username must be less than 12 characters")
elif not username.find(" ")==-1:
    print("There are spaces in the username , please remove them")
elif not username.isalpha():
    print("The username contains numbers,please remove them")
else:
    print(f"Welcome {username}")