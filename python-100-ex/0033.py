m, n = map(int, input().split())
count = 0
snt = True
if m < n:
    for j in range(m, n + 1):
        if j > 1:
            snt = True

            for i in range(2, j):
                if j % i == 0:
                    snt = False
                    break

            if snt:
                count += 1
print(count)
