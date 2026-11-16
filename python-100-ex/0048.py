n = int(input())
nnumbers = list(map( int, input().split()))

count = 0
tong = 0

if len( nnumbers) != n:
    print( "Nhap sai so luong phan tu")
    exit()
for i in nnumbers:
    if nnumbers [i] % 5 == 0:
        count += 1
        tong += nnumbers [i]
        print (nnumbers [i], end= " ")

if count == 0:
    print ("-", end="")

print()
print(tong)