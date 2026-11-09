m, n = map(int, input().split())
tong = 0
count = 0
snt = False
for i in range(m, n + 1):
    if i > 1:
        snt = True

        for j in range(2, i):
            if i % j == 0:
                snt = False
                break

        if snt:
            tong += i
            count += 1

print(f"{tong / count:.2f}")
