n = int(input())
demuoc = 0
for i in range(1, n + 1):
    if n % i == 0:
        demuoc += 1
print(demuoc)
