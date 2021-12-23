
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
onef = 0
twof = 0
threef = 0
fourf = 0
fivef = 0
sixf = 0
sevenf = 0
eightf = 0
ninef = 0
tenf = 0
elevenf = 0
twelvef = 0
gamma = 0
gammaBinary = ""
epsilon = 0
epsilonBinary = ""

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
if one1 > one0:
    onef = 1
else:
    onef = 0

if two1 > two0:
    twof = 1
else:
    twof = 0

if three1 > three0:
    threef = 1
else:
    threef = 0

if four1 > four0:
    fourf = 1
else:
    fourf = 0

if five1 > five0:
    fivef = 1
else:
    fivef = 0
    
if six1 > six0:
    sixf = 1
else:
    sixf = 0

if seven1 > seven0:
    sevenf = 1
else:
    sevenf = 0

if eight1 > eight0:
    eightf = 1
else:
    eightf = 0

if nine1 > nine0:
    ninef = 1
else:
    ninef = 0

if ten1 > ten0:
    tenf = 1
else:
    tenf = 0

if eleven1 > eleven0:
    elevenf = 1
else:
    elevenf = 0

if twelve1 > twelve0:
    twelvef = 1
else:
    twelvef = 0

gammaBinary += str(onef) + str(twof) + str(threef) + str(fourf) + str(fivef) + str(sixf) + str(sevenf) + str(eightf) + str(ninef) + str(tenf) + str(elevenf) + str(twelvef)

print("Gamma rate:", gammaBinary)
gamma = int(gammaBinary, 2)
print("to decimal", gamma)

i = 0
while i < len(gammaBinary):
    if gammaBinary[i] == '1':
        epsilonBinary += '0'
    else:
        epsilonBinary += '1'
    i += 1

print("Epsilon rate:", epsilonBinary)
epsilon = int(epsilonBinary, 2)
print("to decimal", epsilon)

print("Product:", epsilon * gamma)
print(ten1, ten0)

    