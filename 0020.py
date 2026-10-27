n = int(input())
to5k = n // 5000
to2k = (n % 5000) // 2000
to1k = (n % 5000 % 2000) // 1000
print(to5k, to2k, to1k)
