import re

match_fruits = r"fr(uits)*"
match_vegetables = r"veg(etables)*"

choice = input("Information on 'fruits' or 'vegetables?' ").lower()
if re.match(match_fruits, choice):
  import Fruits_OOP.py
elif re.match(match_vegetables, choice):
  import Vegetables_OOP.py
else:
  print("Invalid choice.")
