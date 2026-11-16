n = int(input())
nnumbers = list(map(int, input().split()))

if len(nnumbers) != n:
    print("Nhap sai so luong phan tu")
else:
    print(sum(nnumbers))

