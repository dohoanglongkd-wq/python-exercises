x = int(input())
tong = 0
while x > 0:
    tong += x % 10
    x //= 10
print(tong % 10)
if tong % 10 == 9:
    print("may man")
else:
    print("chua may man")
