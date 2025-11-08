weight = input("Weight: ")
unit = input("kilograms(k) or pounds(lbs)?: ")

if unit.upper() == "K" or unit == "kilograms" or unit == "Kilograms":
  new_weight = int(weight) * 0.4
  print(f"You are {new_weight} pounds")

elif unit.upper() == "L" or unit == "lbs" or unit== "pounds":
  new_weight = int(weight) / 0.4
  print(f"You are {new_weight} kilos")

else:
  print("Invalid input")