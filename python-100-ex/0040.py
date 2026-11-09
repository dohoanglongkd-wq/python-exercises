k = int(input())
count = 0
n = 0
while count < k:
    scp = False

    for i in range (0, int(n**0.5) + 1):
        if n == i**2:
            scp = True
            break

    if scp:
        count += 1
        print(n, end=" ")

    n += 1