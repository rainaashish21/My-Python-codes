import math

x=9.6

print(math.pi)
print(math.e)
print(math.sqrt(8))
print(math.ceil(x))
print(math.floor(x))


radius= float(input("Enter the radius of the circle : "))

circumference = 2 * math.pi *radius
print(f" The circumference of circle is  {round(circumference,2)}")
area= math.pi * pow(radius,2)
print(area)

a= float(input("enter the first side of the triangle: "))
b = float(input("Enter the 2nd side of the triangle: "))

c=pow(a,2)
d=pow(b,2)
Hyp=c+d
print(round(math.sqrt(Hyp),2))
