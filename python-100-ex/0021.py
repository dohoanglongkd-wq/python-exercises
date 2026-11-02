n = int(input())
if n <= 30:
    Tien = 1 * 12000 + (n - 1) * 10000
elif n == 0:
    Tien = 0
else:
    Tien = 1 * 12000 + 29 * 10000 + (n - 30) * 9000
print(Tien)
