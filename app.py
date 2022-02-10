print("Welcome to weight unit converter!")

weight = float(input("What's your weight? Numbers only, please: "))
unit_input = input("(K)g or (L)bs? Type letter, please: ")

if unit_input.upper() == "K":
    unit = "lbs"
    weight //= 0.45
else:
    unit = "kg"
    weight *= 0.45

print(f"Your weight is {weight}{unit}")
