n = int(input())
nnumbers = list (map(int, input().split()))
tong = 0

if len(nnumbers) != n:
    print("Nhap sai so luong phan tu")
    exit()
for i in range(len(nnumbers)):
    if i % 2 == 0:
        tong += nnumbers[i]
print(tong)
