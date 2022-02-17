#there is no block scope in python

# if 3 > 2:
#     a_variable = 10

game_level = 3   
def create_enemy():
    enemies = ["skeleton", "zombie", "alien"]

    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)