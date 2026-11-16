n = int(input())
nnumbers = list(map(int, input().split()))

if len(nnumbers) != n:
    print("Nhap sai so luong phan tu")
    exit()
    
for i in range (len(nnumbers)):
    if nnumbers [i] > 0:
        print(nnumbers[i], end = " ")