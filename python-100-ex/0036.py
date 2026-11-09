m, n = map(int, input().split())
gcd = 1
for i in range(1, min(m, n) + 1):
    if m % i == 0 and n % i == 0:
        gcd = i
print(gcd)

# approach 2(euclidean algorithm) - AI Suggested
m, n = map(int, input().split())
def gcd(m, n):
    while n != 0:
        m, n = n, m % n
    return m
