sodien = int(input())
if sodien <= 50:
    Tien = sodien * 600
elif sodien <= 100:
    Tien = 50 * 600 + (sodien - 50) * 800
elif sodien <= 200:
    Tien = 50 * 600 + 50 * 800 + (sodien - 100) * 1100
else:
    Tien = 50 * 600 + 50 * 800 + 100 * 1100 + (sodien - 200) * 1500
print(Tien)
