n = int (input())
nnumbers = list(map( int, input().split()))
maximum = nnumbers [0]

if len( nnumbers) != n:
    print( "Nhap sai so luong phan tu")
    exit()
# for i in range (len(nnumbers)):
#     if nnumbers [i] > maximum:
#         maximum = nnumbers [i]

# print(maximum, nnumbers.index(maximum))

#methods2:
for i in range (len(nnumbers)):
    maximum = max ( maximum, nnumbers [i])

print(maximum, nnumbers.index(maximum))

#Approach2:
# print (max(nnumbers), nnumbers.index( max( nnumbers)))

# #Approach3:
# for i in nnumbers:
#     if i > maximum:
#         maximum = i

# print ( maximum, nnumbers.index( maximum))

# #Approach4: AI suggested - Using enumerate()
# loco_index = 0

# for i, x in enumerate( nnumbers):
#     if x > maximum:
#         maximum = x
#         loco_index = i

# print( maximum, loco_index)

# #Approach5: AI suggested - Using enumerate() with max()
# maxi = max(nnumbers)

# for i, x in enumerate(nnumbers):
#     if x == maxi:
#         print( maxi, i)
#         break