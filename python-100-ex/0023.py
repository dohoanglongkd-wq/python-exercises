n = int(input())
dem = 0
for i in range(1, n + 1):
    if i % 3 == 0:
        print(i, end=" ")
        dem += 1
if dem == 0:
    print("-")
