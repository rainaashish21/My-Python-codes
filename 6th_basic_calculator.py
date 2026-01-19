operator= input("Please enter the operator (+ or - or * or /) : ")
num1 = float(input("Please enter the first number : "))
num2 = float(input("Please enter the second number : "))

if operator =="+":
    result = num1 +num2
    print(round(result,2))

elif operator =="-":
    result = num1-num2
    print(round(result,2))

elif operator =="*":
    result = num1*num2
    print(round(result,2))

elif operator =="/":
    result = num1 / num2
    print(round(result,2))
else:
    print(f"{operator} is not there,please enter the correct operator")
