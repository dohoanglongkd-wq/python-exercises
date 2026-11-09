n = int(input())
scp = False
for i in range (1, n + 1):
    if n == i**2:
        scp = True
        break
print("Yes" if scp else "No")