#vegetables_oop.py: Vegetables information module

#Vegetables super class
class Vegetables():
  vegetable_name = ""
  
  def __init__(self,name):
    self.name = name
    
#Broccoli sub class
class Broccoli(Vegetables):
  def __init__(self,name):
    self.vegetable_name = "broccoli"
    super().__init__(name)
    
  def desc(self):
    if choose_color in ("green","bright green","dark green"):
      print("Green broccoli\n  An edible green plant.")
    elif choose_color in ("yellow","discolored"):
      print("Rotting broccoli\n  An expiring plant.")
      
  def calorie(self):
    print("Calories(in 148g):\n  50kcal") 
    
  def nutrition(self):
    print("Nutrition(in 148g):\n  Total Fat: 0.5g\n  Sodium: 49mg"
          "\n  Potassium: 468mg\n  Total Carbohydrate: 10g\n  Protein: 4.2g")
    
#Spinach sub class
class Spinach(Vegetables):
  def __init__(self,name):
    self.vegetable_name = "spinach"
    super().__init__(name)
    
  def desc(self):
    if choose_color in ("green","bright green"):
      print("Green spinach\n  An edible, leafy green, flowering plant.")
    elif choose_color in ("black","dark","dark green","mushy","discolored"):
      print("Rotting spinach\n  A spoiled/beginning to spoil, plant.")
      
  def calorie(self):
    print("Calories(in 100g):\n  23.18kcal")
    
  def nutrition(self):
    print("Nutrition(in 100g):\n  Total Fat: 0.4g\n  Sodium: 79mg"
          "\n  Potassium: 558mg\n  Total Carbohydrate: 3.6g\n  Protein: 2.9g")
    
#Lettuce sub class
class Lettuce(Vegetables):
  def __init__(self,name):
    self.vegetable_name = "lettuce"
    super().__init__(name)
    
  def desc(self):
    if choose_color in ("green","bright green","dark green"):
      print("Green lettuce\n  A leafy green plant.")
    elif choose_color in ("discolored","brown","black"):
      print("Rotting lettuce\n  An expiring leafy plant.")
      
  def calorie(self):
    print("Calories(in 36g):\n  5kcal")
    
  def nutrition(self):
    print("Nutrition(in 36g):\n  Total Fat: 0.1g\n  Sodium: 10mg"
          "\n  Potassium: 70mg\n  Total Carbohydrate: 1g\n  Protein: 0.5g")
    
#Onion sub class
class Onion(Vegetables):
  def __init__(self,name):
    self.vegetable_name = "onion"
    super().__init__(name)
    
  def desc(self):
    if choose_color in ("yellow","red","white"):
      print("Common onion\n  A bulb plant.")
    elif choose_color in ("discolored","brown","black"):
      print("Rotting onion\n  An expiring bulb plant.")
      
  def calorie(self):
    print("Calories(in 110g):\n  44kcal")
    
  def nutrition(self):
    print("Nutrition(in 110g):\n  Total Fat: 0.1g\n  Sodium: 4mg"
          "\n  Potassium: 161mg\n  Total Carbohydrate: 10g\n  Protein: 1.2g")
    
#Dictionairy for vegetable string and function
vegetable_dict = {
  "broccoli":Broccoli,
  "spinach":Spinach,
  "lettuce":Lettuce,
  "onion":Onion
}

#user input and printing information
choose_color = input("What color is the vegetable? ").lower()

for name,value in vegetable_dict.items():
  print(" {}".format(name))
  
choose_vegetable = (input("Which vegetable would you like information on? ")
                    .lower())
if choose_vegetable in vegetable_dict:
  vegetable_dict[choose_vegetable]("").desc()
  vegetable_dict[choose_vegetable]("").calorie()
  vegetable_dict[choose_vegetable]("").nutrition()
else:
  print("No information on {} {}.".format(choose_color,choose_vegetable))
