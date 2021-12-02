# Hello!
with open('Day1/input.txt') as f:
    depths = f.readlines()

i = 0
while i < len(depths):
    depths[i] = int(depths[i])
    i += 1

this = 0
that = 1
andThis = 2
count = 0
sum1 = 0
sum2 = 0
while andThis < len(depths):
    if (this == 0):
        sum2 = depths[this] + depths[that] + depths[andThis]
        this += 1
        that += 1
        andThis += 1
        continue

    sum1 = sum2
    sum2 = depths[this] + depths[that] + depths[andThis]
    if (sum1 < sum2):
        count += 1
    
    this += 1
    that += 1
    andThis += 1

print("Number of group increases =", count)