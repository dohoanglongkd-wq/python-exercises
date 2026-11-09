#AI suggested approach in line 7 (Sep statement) )
t, m = map(int, input().split())
def gcd(t, m):
    while m !=0:
        t, m = m, t % m
    return t
print((t // gcd(t, m)), "/", (m // gcd(t, m)), sep="")
# or print((t // gcd(t, m)), (m // gcd(t, m)), sep="/")
