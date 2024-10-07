# Character: Main Class
# Hero: controlled by user
# Enemy

import random


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
    return f"\nName: {self.get_name()}\nHP: {self.get_health_points()}\nLevel: {self.get_level()}"

  def attack(self, target):
    damage = random.randint(self.__level * 2, self.__level * 4)
    target.receive_attack(damage)
    print(f"{self.get_name()} attacked {target.get_name()} and caused {damage} damage!!!")

  def receive_attack(self, damage):
    self.__health_points -= damage
    if(self.__health_points < 0):
      self.__health_points = 0



# Hero Class  
class Hero(Character):
  def __init__(self, name, health_points, level, special_attack) -> None:
    super().__init__(name, health_points, level)
    self.__special_attack = special_attack

  def get_special_attack(self):
    return self.__special_attack
  
  def show_details(self):
    return f"{super().show_details()}\nSpecial Attack: {self.get_special_attack()}"

  def special_attack(self, target):
    damage = self.get_level() * 5
    damage = random.randint(self.get_level() * 5, self.get_level() * 8)
    target.receive_attack(damage)
    print(f"{self.get_name()} used special attack {self.get_special_attack()} in {target.get_name()} and caused {damage} damage!!!")
  

# Enemy Class
class Enemy(Character):
  def __init__(self, name, health_points, level, type) -> None:
    super().__init__(name, health_points, level)
    self.__type = type

  def get_type(self):
    return self.__type
  
  def show_details(self):
    return f"{super().show_details()}\nType: {self.get_type()}"
    

class Game:
  def __init__(self) -> None:
    self.hero = Hero(name="Hero", health_points=100, level=5, special_attack="Super Strengh")
    self.enemy = Enemy(name="Enemy", health_points=80, level=5, type="Fly")

  def start_battle(self):
    print("Start Battle")

    while (self.hero.get_health_points() > 0 and self.enemy.get_health_points() > 0):
      print("\nCharacters Details")
      print(self.hero.show_details())
      print(self.enemy.show_details())

      input("\nPress Enter to attack...")
      choose = input("Choose (1 - Normal Attack, 2 - Special Attack): ")

      if choose == "1":
        self.hero.attack(self.enemy)
      elif choose == "2":
        self.hero.special_attack(self.enemy)
      else:
        print(f"invalid choose")

      if self.enemy.get_health_points() > 0:
        self.enemy.attack(self.hero)


    if self.hero.get_health_points() > 0:
      print("\nCongratulations, you won the battle!!!")
    else:
      print("\nYou were defeated :(")


game = Game()
game.start_battle()