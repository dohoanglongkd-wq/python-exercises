t, m = map(int, input().split())
def gcd(t, m):
    while m !=0:
        t, m = m, t % m
    return t
print(str(t // gcd(t, m)) + "/" + str(m // gcd(t, m)))