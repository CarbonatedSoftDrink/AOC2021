
with open('Day3/input.txt') as f: 
    diag = f.readlines()

one1 = 0
one0 = 0
two1 = 0
two0 = 0
three1 = 0
three0 = 0
four1 = 0
four0 = 0
five1 = 0
five0 = 0
six1 = 0
six0 = 0
seven1 = 0
seven0 = 0
eight1 = 0
eight0 = 0
nine1 = 0
nine0 = 0
ten1 = 0
ten0 = 0
eleven1 = 0
eleven0 = 0
twelve1 = 0
twelve0 = 0
list1 = []
listFinal =[]
higher = 0

i = 0
while (i < len(diag)):
    if diag[i][0] == '1':
        one1 += 1
    else:
        one0 += 1
    
    if diag[i][1] == '1':
        two1 += 1
    else:
        two0 += 1

    if diag[i][2] == '1':
        three1 += 1
    else:
        three0 += 1

    if diag[i][3] == '1':
        four1 += 1
    else:
        four0 += 1

    if diag[i][4] == '1':
        five1 += 1
    else:
        five0 += 1

    if diag[i][5] == '1':
        six1 += 1
    else:
        six0 += 1
    
    if diag[i][6] == '1':
        seven1 += 1
    else:
        seven0 += 1

    if diag[i][7] == '1':
        eight1 += 1
    else:
        eight0 += 1

    if diag[i][8] == '1':
        nine1 += 1
    else:
        nine0 += 1

    if diag[i][9] == '1':
        ten1 += 1
    else:
        ten0 += 1

    if diag[i][10] == '1':
        eleven1 += 1
    else:
        eleven0 += 1

    if diag[i][11] == '1':
        twelve1 += 1
    else:
        twelve0 += 1
    i += 1

# /////////////

i = 0
if one1 >= one0:
    higher = 1
else:
    higher = 0
while i < len(diag):
    if diag[i][0] == str(higher):
        list1.append(diag[i])
    i += 1
#print("first:", list1)
print("length:", len(list1))
print(two1, two0)

if two1 >= two0:
    higher = 1
else:
    higher = 0
j = 0
while j < len(list1):
    if list1[j][1] != str(higher):
        list1.pop(j)
    j += 1

if three1 >= three0:
    higher = 1
else:
    higher = 0
j = 0
while j < len(list1):
    if list1[j][2] != str(higher):
        list1.remove(list1[j])
    j += 1

if four1 >= four0:
    higher = 1
else:
    higher = 0
j = 0
while j < len(list1):
    if list1[j][3] != str(higher):
        list1.remove(list1[j])
    j += 1

if five1 >= five0:
    higher = 1
else:
    higher = 0
j = 0
while j < len(list1):
    if list1[j][4] != str(higher):
        list1.remove(list1[j])
    j += 1

if six1 >= six0:
    higher = 1
else:
    higher = 0
j = 0
while j < len(list1):
    if list1[j][5] != str(higher):
        list1.remove(list1[j])
    j += 1

if seven1 >= seven0:
    higher = 1
else:
    higher = 0
j = 0
while j < len(list1):
    if list1[j][6] != str(higher):
        list1.remove(list1[j])
    j += 1

if eight1 >= eight0:
    higher = 1
else:
    higher = 0
j = 0
while j < len(list1):
    if list1[j][7] != str(higher):
        list1.remove(list1[j])
    j += 1

if nine1 >= nine0:
    higher = 1
else:
    higher = 0
j = 0
while j < len(list1):
    if list1[j][8] != str(higher):
        list1.remove(list1[j])
    j += 1

if ten1 >= ten0:
    higher = 1
else:
    higher = 0
j = 0
while j < len(list1):
    if list1[j][9] != str(higher):
        list1.remove(list1[j])
    j += 1

if eleven1 >= eleven0:
    higher = 1
else:
    higher = 0
j = 0
while j < len(list1):
    if list1[j][10] != str(higher):
        list1.remove(list1[j])
    j += 1

if twelve1 >= twelve0:
    higher = 1
else:
    higher = 0
j = 0
while j < len(list1):
    if list1[j][11] != str(higher):
        list1.remove(list1[j])
    j += 1

print(list1)

    