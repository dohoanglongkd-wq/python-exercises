m, n = map (int, input().split())
count = 0
snt = True
if m < n:
    for j in range (2, n+1):
        for i in range (2, j)
        if j % i == 0:
            snt = False
            count += 1
elif n <= 1 and m <= 1:
    snt = False
print (count)