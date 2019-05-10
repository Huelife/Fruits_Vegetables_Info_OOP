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

#Dictionairy for fruit string and function
fruit_dict = {
  "apple": Apple,
  "banana": Banana
}
#user input and printing information
choose_color = input("What color is the fruit? ").lower()

choose_fruit = input("Which fruit would you like information on? ").lower()
if choose_fruit in fruit_dict:
  fruit_dict[choose_fruit]("").desc()
  fruit_dict[choose_fruit]("").calorie()
  fruit_dict[choose_fruit]("").nutrition()
else:
  print("No information on {}.".format(choose_color+" "+choose_fruit))
  
