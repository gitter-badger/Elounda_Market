#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

# -------------- READ WRITE FILES ----------------------
with open('write.txt', 'w') as a:
    print('[BARCODE]', file=a)
with open("read.txt", 'r') as q:
    line = q.read().splitlines()
stathero = '5200310'


# Mayogiannis = 5200310
# Koukoutaris = 5202535

# ---------------FUNCTION HERE---------------------
def calculate(code):
    code = stathero + code
    athrisma = 0
    for y in range(len(code)):
        if y % 2 == 0:
            athrisma += int(code[y]) * 1
        else:
            athrisma += int(code[y]) * 3
    micro = athrisma % 10
    if micro == 0:
        last_digit = 0
    else:
        last_digit = 10 - micro
    barcode = code + str(last_digit)
    return barcode


# --------------MAIN PROGRAM----------------------
for z in line:
    with open('write.txt', 'a') as a:
        print(calculate(z), file=a)