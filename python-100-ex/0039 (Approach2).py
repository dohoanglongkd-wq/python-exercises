n = int(input())
scp = False
for i in range (1, int(n**0.5) + 1): #AI suggested change: range (1, n + 1) to range (1, int(n**0.5) + 1) for efficiency
    if n == i**2:
        scp = True
        break
print("Yes" if scp else "No")