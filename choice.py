#choice.py: Choosing between fruits and vegetables information

import re

#user input matchs fr+ and veg+
match_fruits = r"fr(uits)*"
match_vegetables = r"veg(etables)*"

#user can choose between fruits or vegetables, but repeats if neither
while True:
  try:
    choice = (input("Nutrition information on 'fruits' or 'vegetables?' ")
              .lower())
  except ValueError:
    continue
  else:
    if re.match(match_fruits, choice):
      import fruits_oop.py    
    elif re.match(match_vegetables, choice):
      import vegetables_oop.py
    break
    else:
      print("{} is an invalid choice.".format(choice))
      continue
