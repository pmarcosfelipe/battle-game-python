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
    return f"\nName: {self.get_name()}\nHP: {self.get_health_points()}\nLevel: {self.get_level()}"

  def attack(self, target):
    damage = self.__level * 2
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
    self.enemy = Enemy(name="Enemy", health_points=50, level=2, type="Fly")

  def start_battle(self):
    print("Start Battle")

    while (self.hero.get_health_points() > 0 and self.enemy.get_health_points() > 0):
      print("\nCharacteres Details")
      print(self.hero.show_details())
      print(self.enemy.show_details())

      input("\nPress Enter to  attack...")
      choose = input("Choose (1 - Normal Attack, 2 - Special Attack)")

      if choose == "1":
        self.hero.attack(self.enemy)
      else:
        print(f"invalid choose")

    if self.hero.get_health_points() > 0:
      print("\nCongratulations, you won the battle")
    else:
      print("\nYou were defeated!")


game = Game()
game.start_battle()