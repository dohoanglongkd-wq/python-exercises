a = int(input())
to5k = a // 5000
to2k = (a % 5000) // 2000
to1k = (a % 5000 % 2000) // 1000
print(to5k, to2k, to1k)
