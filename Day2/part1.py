# Hello!
x = 0
y = 0
product = 0
''' intended to put all my code into this function
def extract(item, numx, numy):
    #num += 9
    if (item[0] == 'f'):
        numx += int(item[8])
    elif (item[0] == 'd'):
        numy += int(item[5])
    elif (item[0] == 'u'):
        numy += int(item[3])
'''

with open('Day2/input.txt') as f: 
    directions = f.readlines()

i = 0
while i < len(directions):
    if (directions[i][0] == 'f'):
        x += int(directions[i][8])
    elif (directions[i][0] == 'd'):
        y += int(directions[i][5])
    elif (directions[i][0] == 'u'):
        y -= int(directions[i][3])

    i += 1

product = x * y

print("x =", x)
print("y =", y)
print("Product of horizontal and vertical =", product)