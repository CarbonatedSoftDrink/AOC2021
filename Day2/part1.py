# Hello!
x = 0
y = 0
product = 0

with open('Day2/input.txt') as f:
    directions = f.readlines()

i = 0
while i < len(directions):
    if directions[0] == 'f':
        x += int(directions[9])

    i += 1


print("x =", x)
print("y =", y)
print("Product of horizontal and vertical =", product)