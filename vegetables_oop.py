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
    print("Calories(in 148 g):\n  50 kcal") 
    
  def nutrition(self):
    print("Nutrition(in 148 g):\n  Total Fat: 0.5 g\n  Sodium: 49 mg"
          "\n  Potassium: 468 mg\n  Total Carbohydrate: 10 g\n  Protein: 4.2 g")
    
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
    print("Calories(in 100 g):\n  23.18 kcal")
    
  def nutrition(self):
    print("Nutrition(in 100 g):\n  Total Fat: 0.4 g\n  Sodium: 79 mg"
          "\n  Potassium: 558 mg\n  Total Carbohydrate: 3.6 g\n  Protein: 2.9 g")
    
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
    print("Calories(in 36 g):\n  5 kcal")
    
  def nutrition(self):
    print("Nutrition(in 36 g):\n  Total Fat: 0.1 g\n  Sodium: 10 mg"
          "\n  Potassium: 70 mg\n  Total Carbohydrate: 1 g\n  Protein: 0.5 g")
    
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
    print("Calories(in 110 g):\n  44 kcal")
    
  def nutrition(self):
    print("Nutrition(in 110 g):\n  Total Fat: 0.1 g\n  Sodium: 4 mg"
          "\n  Potassium: 161 mg\n  Total Carbohydrate: 10 g\n  Protein: 1.2 g")
    
#Dictionary for vegetable string and function
vegetable_dict = {
  "broccoli":Broccoli,
  "spinach":Spinach,
  "lettuce":Lettuce,
  "onion":Onion
}

#user input and printing information
choose_color = input("What color is the vegetable? ").lower()

[print(" {}".format(name)) for name,value in vegetable_dict.items()]
  
choose_vegetable = (input("Which vegetable would you like information on? ")
                    .lower())
if choose_vegetable in vegetable_dict:
  vegetable_dict[choose_vegetable]("").desc()
  vegetable_dict[choose_vegetable]("").calorie()
  vegetable_dict[choose_vegetable]("").nutrition()
else:
  print("No information on {} {}.".format(choose_color,choose_vegetable))
