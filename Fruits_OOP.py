#Fruits super class
class Fruits():
  fruit_name = ""
  def __init__(self,name):
    self.name = name
#Apple sub class
class Apple(Fruits):
  def __init__(self,name):
    self.fruit_name = "apple"
    super().__init__(name)
  
  def desc(self):
    if choose_color == "green":
      print("Green apple\n  An apple that isn't ripe.")
    elif choose_color == "red":
      print("Red apple\n  A ripe apple.")

  def calorie(self):
    print("Calories(in 182g):\n  95")
    
  def nutrition(self):
    print("Nutrition(in 182g):\n  Total Fat: 0.3g\n  Sodium: 2mg\n  Potassium: 195mg\n  Total Carbohydrate: 25g\n  Protein: 0.5g")
#Banana sub class
class Banana(Fruits):
  def __init__(self,name):
    self.fruit_name = "banana"
    super().__init__(name)

  def desc(self):
    if choose_color in ("green","dark green","light green"):
      print("Green banana\n  A banana that isn't ripe.")
    elif choose_color == "yellow":
      print("Yellow banana\n  A ripe banana.")
    
  def calorie(self):
    print("Calories(in 118g):\n  105")
    
  def nutrition(self):
    print("Nutrition(in 118g):\n  Total Fat: 0.4g\n  Sodium: 1mg\n  Potassium: 422mg\n  Total Carbohydrate: 27g\n  Protein: 1.3g")
#Orange sub class
class Orange(Fruits):
  def __init__(self,name):
    self.fruit_name = "orange"
    super().__init__(name)

  def desc(self):
    if choose_color == "light green":
      print("Light green orange\n  An unripened orange.")
    elif choose_color in ("yellow","orange","green","dark green"):
      print("Yellow orange\n  A ripe orange.")
    
  def calorie(self):
    print("Calories(in 100g):\n  47")
    
  def nutrition(self):
    print("Nutrition(in 100g):\n  Total Fat: 0.1g\n  Sodium: 0mg\n  Potassium: 181mg\n  Total Carbohydrate: 12g\n  Protein: 0.9g")
#Strawberry sub class
class Strawberry(Fruits):
  def __init__(self,name):
    self.fruit_name = "strawberry"
    super().__init__(name)

  def desc(self):
    if choose_color in ("light green","green","white"):
      print("White-green strawberry\n  An unripened strawberry.")
    elif choose_color in ("red","bright red","deep red","dark red","burgundy"):
      print("Red strawberry\n  A ripe strawberry.")
    
  def calorie(self):
    print("Calories(in 100g):\n  33")
    
  def nutrition(self):
    print("Nutrition(in 100g):\n  Total Fat: 0.3g\n  Sodium: 1mg\n  Potassium: 153mg\n  Total Carbohydrate: 8g\n  Protein: 0.7g")
#Dictionairy for fruit string and function
fruit_dict = {
  "apple": Apple,
  "banana": Banana,
  "orange": Orange,
  "strawberry": Strawberry
}
#user input and printing information
choose_color = input("What color is the fruit? ").lower()
for name,value in fruit_dict.items():
  print(" "+name)
choose_fruit = input("Which fruit would you like information on? ").lower()
if choose_fruit in fruit_dict:
  fruit_dict[choose_fruit]("").desc()
  fruit_dict[choose_fruit]("").calorie()
  fruit_dict[choose_fruit]("").nutrition()
else:
  print("No information on {} {}.".format(choose_color,choose_fruit))
