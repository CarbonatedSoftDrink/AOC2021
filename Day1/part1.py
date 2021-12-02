# Hello!
with open('Day1/input.txt') as f:
    depths = f.readlines()

i = 0
while i < len(depths):
    depths[i] = int(depths[i])
    i += 1

this = 0
that = 1
count = 0
while that < len(depths):
    if depths[this] < depths[that]:
        count += 1
    this += 1
    that += 1

print("Number of increases =", count)