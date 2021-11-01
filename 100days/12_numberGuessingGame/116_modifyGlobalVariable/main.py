#Modifying global scope

enemies = 1

def increase_enemies():
    # global enemies #telling global variable outside of function
    # enemies += 1
    print(f"enemies inside function: {enemies}")
    return enemies + 1

increase_enemies() #output 2
print(f"enemies outside function: {enemies}") #output 1 

