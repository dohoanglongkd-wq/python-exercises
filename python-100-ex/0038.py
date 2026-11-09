k = int(input())
snt = True
count = 0
n = 2
while count < k:
    snt = True

    for i in range (2, n): #AI suggested (Range to n)
        if n % i == 0:
            snt = False
            break

    if snt:
        count += 1
        print (n, end=" ")

    n += 1