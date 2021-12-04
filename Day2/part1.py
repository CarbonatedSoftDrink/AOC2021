# Hello!
x = 0
y = 0
product = 0

def extract(item):
    x += 9
    if (item[0] == 'f'):
        return int(item[8])
    elif (item[0] == 'd'):
        return int(item[5])
    elif (item[0] == 'u'):
        return int(item[3])

with open('Day2/input.txt') as f:
    directions = f.readlines()

i = 0
while i < len(directions):
    x += extract(directions[i])

    i += 1


print("x =", x)
print("y =", y)
print("Product of horizontal and vertical =", product)