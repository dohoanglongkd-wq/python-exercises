n = int(input())
tong = 0
for i in range(1, n + 1):
    if n > 0 and i % 3 == 0 and i % 5 == 0:
        tong += i
print(tong)