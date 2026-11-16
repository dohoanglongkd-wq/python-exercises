a = list(map( int, input().split()))
tong = 0
count = 0

for i in a:
    snt = True

    if i < 2:
        snt = False
    else:
        for j in range (2, int( i ** 0.5) + 1):
            if i % j == 0:
                snt = False
                break
            
    if snt:
        tong += i
        count += 1
        print( i, end= " ")

if count == 0:
    print( "-")

print()
print( tong)

