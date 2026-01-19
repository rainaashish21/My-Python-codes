Principal =0
rate =0
time= 0

while Principal<=0:
    Principal = float(input("Enter the Principal amount : "))
    if Principal <=0:
        print("Please enter the correct principal amount")

while rate<=0:
    rate = float(input("Enter the Interest RAte : "))
    if rate <=0:
        print("Please enter the correct Interest rate")

while time<=0:
    time = int(input("Enter the time (in years) : "))
    if time <=0:
        print("Please enetr the correct time (in years)")

print(Principal)
print(rate)
print(time)

total = Principal * pow((1+rate/100),time)
print(f"Your amount after {time} years is {total:.2f}")

while True:
    Principal = float(input("Enter the Principal amount : "))
    if Principal <=0:
        print("Please enter the correct principal amount")
    else:
        break
while True:
    rate = float(input("Enter the Interest RAte : "))
    if rate <=0:
        print("Please enter the correct Interest rate")
    else:
        break
while True:
    time = int(input("Enter the time (in years) : "))
    if time <=0:
        print("Please enetr the correct time (in years)")
    else:
        break
print(Principal)
print(rate)
print(time)

total = Principal * pow((1+rate/100),time)
print(f"Your amount after {time} years is {total:.2f}")
