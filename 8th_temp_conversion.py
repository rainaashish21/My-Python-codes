unit = input("IS THIS TEMPERATURE in Celsius or Fahrenheit (C or F) : ")
temp =float(input("Enter the temperature : "))

if unit =="C":
    temp = round((9*temp)/5 +32,1)
    print(f" The temperature in Fahreheit is {temp} degree F ")
elif unit =="F":
    temp = round(((temp-32)*5)/9,1)
    print(f"The temperature in Celsius is {temp} degree C")
else:
    print(f"{unit} is an invalid input of measurement")