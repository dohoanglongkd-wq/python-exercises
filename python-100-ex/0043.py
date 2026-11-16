n = int(input())
nnumbers = list(map(int, input().split()))
count = 0

if len(nnumbers) != n:
    print("Nhap sai so luong phan tu")
    exit()
for i in range (len(nnumbers)):
    if nnumbers [i] % 2 == 0:
        count += 1
print(count)