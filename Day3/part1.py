
with open('Day3/input.txt') as f: 
    diag = f.readlines()

one1, one0, two1, two0, three1, three0, four1, four0, five1, five0 = 0
i = 0
while (i < len(diag)):
    if diag[0] == '1':
        one1 += 1
    else:
        one0 += 1
    
    if diag[0] == '1':
        two1 += 1
    else:
        two0 += 1

    if diag[0] == '1':
        three1 += 1
    else:
        three0 += 1

    if diag[0] == '1':
        four1 += 1
    else:
        four0 += 1

    if diag[0] == '1':
        five1 += 1
    else:
        five0 += 1

    