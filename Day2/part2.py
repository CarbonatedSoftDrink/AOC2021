# Hello!
x = 0
y = 0
aim = 0
product = 0

with open('Day2/input.txt') as f: 
    directions = f.readlines()

i = 0
while i < len(directions):
    if (directions[i][0] == 'f'):
        x += int(directions[i][8])
        y += int(directions[i][8]) * aim
    elif (directions[i][0] == 'd'):
        aim += int(directions[i][5])
    elif (directions[i][0] == 'u'):
        aim -= int(directions[i][3])

    i += 1

product = x * y

print("x =", x)
print("y =", y)
print("Product of horizontal and vertical =", product)