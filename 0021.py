sokm = int(input())
if sokm <= 30:
    Tien = 1 * 12000 + (sokm - 1) * 10000
elif sokm == 0:
    Tien = 0
else:
    Tien = 1 * 12000 + 29 * 10000 + (sokm - 30) * 9000
print(Tien)
