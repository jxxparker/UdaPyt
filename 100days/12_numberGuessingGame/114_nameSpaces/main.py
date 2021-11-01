# #SCOPE

# enemies = 1
# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside fxn {enemies}")

# increase_enemies()
# print(f"enemies inside fxn {enemies}")


#local scope

# def drink_potion():
#   potion_strength = 2
#   print(potion_strength)


#global scope

player_health = 10

def game():
      
  def drink_potions():
    potion_strength = 2
    print(player_health)

  drink_potions()
print(player_health)