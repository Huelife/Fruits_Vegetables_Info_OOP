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
      print("Yellow broccoli\n  An expiring green plant.")

  def calorie(self):
    print("Calories(in 148g):\n  50")
    
  def nutrition(self):
    print("Nutrition(in 148g):\n  Total Fat: 0.5g\n  Sodium: 49mg\n  Potassium: 468mg\n  Total Carbohydrate: 10g\n  Protein: 4.2g")
    
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
    print("Calories(in 100g):\n  23.18")
    
  def nutrition(self):
    print("Nutrition(in 100g):\n  Total Fat: 0.4g\n  Sodium: 79mg\n  Potassium: 558mg\n  Total Carbohydrate: 3.6g\n  Protein: 2.9g")

#Dictionairy for vegetable string and function
vegetable_dict = {
  "broccoli": Broccoli,
  "spinach": Spinach
}
#user input and printing information
choose_color = input("What color is the vegetable? ").lower()

choose_vegetable = input("Which vegetable would you like information on? ").lower()
if choose_vegetable in vegetable_dict:
  vegetable_dict[choose_vegetable]("").desc()
  vegetable_dict[choose_vegetable]("").calorie()
  vegetable_dict[choose_vegetable]("").nutrition()
else:
  print("No information on {}.".format(choose_color+" "+choose_vegetable))
  
