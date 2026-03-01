#python weight converter

weight = float(input("Enter your weight : "))
unit = input("enter the units (kg or lbs) : ")

if unit == "kg":
    weight = weight * 2.205
    unit = "lbs"
    print(f"your weight is {weight} {unit}")

elif unit == "lbs":
    weight = weight/2.205
    unit = "kg"
    print(f"your weight is {weight} {unit}")

else:
    print(f"the unit is invalid")
