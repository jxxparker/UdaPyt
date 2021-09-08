#there is no block scope

# if 3 > 2:
#     a_variable = 10

game_level =3

def create_enemy():
    enemies = ["skeleon", "zombie", "alien"]

    if game_level < 5:
        new_enemies = enemies[0]

    print(new_enemies)
