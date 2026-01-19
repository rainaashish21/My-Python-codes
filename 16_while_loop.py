name = input("Enter your name : ")
while name == "":
    print("You didn't enter you name ")
    name = input("Enter your name : ")
print(f"Hello {name}")

age = int(input("Enter your age :"))

while age<0:
    print("Age can't be negative")
    age =int(input("Please enter your age : "))
print(f"You are {age} years old")

print(f"HI {name} ,you are {age} years old")


food = input("Enter the food you like (q to quit) :")
while not food =="q":
    print(f"You like {food} ")
    food = input("Enter another food you like (q to quit) :")

print("Bye")


num =int(input("Enter a number between 1 and 10 :"))

while num<1 or num>10:
    print(f"Your number is not valid")
    num =int(input("Enter a number between 1 and 10 :"))
print(f"You number is {num}")