# python compound interest calculator

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("enter your principle amount : "))
    if principle < 0:
        print("principle cannot be negative")
    else:
        break

while True:
    rate = float(input("enter your rate of interest : "))
    if rate < 0:
        print("rate cannot be negative")
    else:
        break

while True:
    time = float(input("enter your time in years : "))
    if time < 0:
        print("time cannot be negative")
    else:
        break

total = principle * pow((1 + rate/100),time)
print(f"balance after {time} years is : {total:.2f}")