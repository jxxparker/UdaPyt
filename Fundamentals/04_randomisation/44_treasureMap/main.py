# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(map)
# print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

position_1 = int(position[0])
position_2 = int(position[1])

map[position_2 - 1][position_1 - 1] = "X" #map[3][1]
#----------------

print(f"{row1}\n{row2}\n{row3}")