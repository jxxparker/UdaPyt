enemies = 1

# def increase_enemies():
#     global enemies #this tells that theres enemies outside of the function
#     enemies += 1
#     print(f"enemies inside function: {enemies}")

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies()
increase_enemies()
print(f"enemies outside function: {enemies}")