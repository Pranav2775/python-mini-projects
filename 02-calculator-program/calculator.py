#Python Calculator

operator = input("Enter the operator (+,-,*,/) : ")
num1 = float(input("enter the value of num 1 : "))
num2 = float(input("enter the value of num 2 : "))

if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    if num2 == 0:
        print("Error : cannot divide by zero")
    else:
        result = num1 / num2
        print(result)
else:
    print("invalid operator")