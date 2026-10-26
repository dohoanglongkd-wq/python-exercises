bienso = int(input())
tong = 0
while bienso > 0:
    tong += bienso % 10
    bienso //= 10
print(tong % 10)
if tong % 10 == 9:
    print("may man")
else:
    print("chua may man")
