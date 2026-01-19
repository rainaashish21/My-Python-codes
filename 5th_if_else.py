response = input("Would you like food?(Y/N) -- ")
if response == "Y":
    print("Have some food")
else:
    print("No food for you")

name= input("Please enter you name : ")
if name=="":
    print("You didn't type in your name")
else:
    print(f" Hello {name}, How are you?")

online = True
if online:
    print("You are online")
else:
    print("you are offline")
