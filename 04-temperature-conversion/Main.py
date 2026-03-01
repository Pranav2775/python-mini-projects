# python temperature converter

units = input("is the unit is in celcius or farhenheite (c/f) : ")
temperature = float(input("enter the temperature : "))

if units == "c":
    temperature = (9*temperature)/5 + 32
    print(f"the temperature is {temperature}f")

elif units == "f":
    temperature = (temperature - 32) * 5 / 9
    print(f"the temperature is {temperature}c")

else:
    print(f"the {units} is totally invalid")