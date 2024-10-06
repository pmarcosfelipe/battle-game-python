# Character: Main Class
# Hero: controlled by user
# Enemy

class Character:
  def __init__(self, name, health_points, level) -> None:
    self.__name = name
    self.__health_points = health_points
    self.__level = level

  def get_name(self):
    return self.__name
  
  def get_health_points(self):
    return self.__health_points
  
  def get_level(self):
    return self.__level
  
  def show_details(self):
    return f"Name: {self.get_name()}\nHP: {self.get_health_points()}\nLevel: {self.get_level()}"


# Hero Class  
class Hero(Character):
  def __init__(self, name, health_points, level, special_attack) -> None:
    super().__init__(name, health_points, level)
    self.__special_attack = special_attack

  def get_special_attack(self):
    return self.__special_attack
  
  def show_details(self):
    return f"{super().show_details()}\nSpecial Attack: {self.get_special_attack()}"
  

# Enemy Class
class Enemy(Character):
  def __init__(self, name, health_points, level, type) -> None:
    super().__init__(name, health_points, level)
    self.__type = type

  def get_type(self):
    return self.__type
  
  def show_details(self):
    return f"{super().show_details()}\nType: {self.get_type()}"
    

hero = Hero(name="Hero", health_points=100, level=5, special_attack="Super Strengh")
print(hero.show_details())

enemy = Enemy(name="Enemy", health_points=50, level=2, type="Fly")
print(enemy.show_details())