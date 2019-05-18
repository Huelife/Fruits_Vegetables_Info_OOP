import re

match_fruits = r"fr(uits)*"
match_vegetables = r"veg(etables)*"

while True:
  try:
    choice = input("Nutrition information on 'fruits' or 'vegetables?' ").lower()
  except ValueError:
    continue
  else:
    if re.match(match_fruits, choice):
      import Fruits_OOP.py
    elif re.match(match_vegetables, choice):
      import Vegetables_OOP.py
    break
    else:
      print("{} is an invalid choice.".format(choice))
      continue
