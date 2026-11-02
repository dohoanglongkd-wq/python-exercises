from math import sqrt

a, b, c = map(int, input().split())
cv = a + b + c
p = cv / 2
s = sqrt(p * (p - a) * (p - b) * (p - c))
if a + b > c and a + c > b and b + c > a:
    print(f"{cv:.1f} {s:.3f}")
