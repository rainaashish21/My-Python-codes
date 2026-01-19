#typecasting = The process of converting one data type to another
name = "Ashish"
age= 24
gpa=9.03
boo=True

print(type(name))
print(type(age))
print(type(gpa))
print(type(boo))

#Explicit
age =float(age)
print(type(age))

age =bool(age)
print(age)
print(type(age))

name=bool(name)
print(name)
print(type(name))

#Implicit
a =100
b=24.32
a=a/b
print(a)
print(type(a))

adjective1= "suspicious"
noun="Lion"
adjective2= "scary"
verb="screech"
adjective3="amazed"
print(f"Today i went to a {adjective1} zoo.")
print(f"There i saw {noun}.")
print(f"{noun} was {adjective2} and {verb}ing.")
print(f"I was {adjective3}.")

#Area and volume of a rectangle
length=float(input("Enter the length of the rectangle : "))
width=float(input("Enter the width of the rectangle : "))
height=float(input("Enter the height of the rectangle : "))
area = length * width
volume = length * width *height
print(f"The area of the rectangle is : {area} m^2 ")
print(f"The volume of the rectangle is :{volume} m^3")

#shopping cart
item =input("what item would you like to buy?  ")
price=float(input("What is the price?  "))
quantity = int(input("How many would you  like to buy? "))

total = price* quantity
print(f"You have bought {quantity} X {item}/s")
print(f"Your total price is : ${round(total,2)}")


#