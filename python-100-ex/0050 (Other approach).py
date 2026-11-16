n = int (input())
nnumbers = list(map( int, input().split()))

if len( nnumbers) != n:
    print( "Nhap sai so luong phan tu")
    exit()

# Approach1:
# nnumbers.sort()
# print( *nnumbers)

# Approach2:
# print( *sorted(nnumbers))

# Approach3:
# nnumbers.sort()

# for x in nnumbers:
#     print( x, end=" ")

# Approach4: Using Buble sort - Self-study
# For i in range (n - 1):
#     for j in range ( n - 1 - i):
#         if nnumbers [j] > nnumbers [j + 1]:
#             nnumbers [j], nnumbers [j + 1] = nnumbers [j + 1], nnumbers [j]
# print( *nnumbers)

# Methods2: AI suggested - Buble sort + Boolean
for i in range (n-1):
    swapped = False

    for j in range (n-1-i):
        if nnumbers [j] > nnumbers [j + 1]:
            nnumbers [j], nnumbers [j + 1] = nnumbers [j + 1], nnumbers [j]
            swapped = True

    if not swapped:
        break
print( *nnumbers)