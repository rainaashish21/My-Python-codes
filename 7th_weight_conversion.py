weight = float(input("Please enter your weight : "))
Unit =input("Kilograms or Pounds (K or L)? ")

if Unit == "K":
    weight = weight *2.025
    Unit = "Lbs"
    print(f"Your weight is {round(weight,1)} {Unit}")
elif Unit =="L":
    weight = weight /2.05
    Unit = "Kgs"
    print(f"Your weight is {round(weight,1)} {Unit}")
else:
    print(f"{Unit} was not available")


