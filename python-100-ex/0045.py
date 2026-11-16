n = int(input())
nnumbers = list (map( int, (input().split())))
tong = 0
count = 0

if len(nnumbers) != n:
    print("Nhap sai so luong phan tu")
    exit()
for i in range (len(nnumbers)):
    if nnumbers[i] % 2 == 0:
        tong += nnumbers[i]
        count += 1

if count > 0:
    print(tong)
else:
    print("-")