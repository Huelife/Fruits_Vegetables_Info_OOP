#fruits_oop.py: Fruits information module

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
    print("Calories(in 182 g):\n  95 kcal")
    
  def nutrition(self):
    print("Nutrition(in 182 g):\n  Total Fat: 0.3 g\n  Sodium: 2 mg"
          "\n  Potassium: 195 mg\n  Total Carbohydrate: 25 g\n  Protein: 0.5 g")
    
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
    print("Calories(in 118 g):\n  105 kcal")
    
  def nutrition(self):
    print("Nutrition(in 118 g):\n  Total Fat: 0.4 g\n  Sodium: 1 mg"
          "\n  Potassium: 422 mg\n  Total Carbohydrate: 27 g\n  Protein: 1.3 g")
    
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
    print("Calories(in 100 g):\n  47 kcal")
    
  def nutrition(self):
    print("Nutrition(in 100 g):\n  Total Fat: 0.1 g\n  Sodium: 0 mg"
          "\n  Potassium: 181 mg\n  Total Carbohydrate: 12 g\n  Protein: 0.9 g")
    
#Strawberry sub class
class Strawberry(Fruits):
  def __init__(self,name):
    self.fruit_name = "strawberry"
    super().__init__(name)
    
  def desc(self):
    if choose_color in ("light green","green","white"):
      print("White-green strawberry\n  An unripened strawberry.")
    elif choose_color in ("red","bright red","dark red","burgundy"):
      print("Red strawberry\n  A ripe strawberry.") 
      
  def calorie(self):
    print("Calories(in 100 g):\n  33 kcal")
    
  def nutrition(self):
    print("Nutrition(in 100 g):\n  Total Fat: 0.3 g\n  Sodium: 1 mg"
          "\n  Potassium: 153 mg\n  Total Carbohydrate: 8 g\n  Protein: 0.7 g")
    
#Dictionary for fruit string and function
fruit_dict = {
  "apple":Apple,
  "banana":Banana,
  "orange":Orange,
  "strawberry":Strawberry
}

#user input and printing information
choose_color = input("What color is the fruit? ").lower()

[print(" {}".format(name)) for name,value in fruit_dict.items()]
  
choose_fruit = input("Which fruit would you like information on? ").lower()
if choose_fruit in fruit_dict:
  fruit_dict[choose_fruit]("").desc()
  fruit_dict[choose_fruit]("").calorie()
  fruit_dict[choose_fruit]("").nutrition()
else:
  print("No information on {} {}.".format(choose_color,choose_fruit))
