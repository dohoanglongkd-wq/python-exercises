n = int( input())
nnumbers = list(map (int, input().split()))
countpositive = 0
countnegative = 0

if len(nnumbers) != n:
    print("Nhap sai so luong phan tu")
    exit()
for i in range (n):
    if nnumbers [i] > 0:
        countpositive += 1  
    elif nnumbers [i] < 0:
        countnegative += 1

print (countpositive, countnegative)
    
if countpositive == 0:
            print ("-")
else:
    for i in range (n):
        if nnumbers [i] > 0:
            print (nnumbers [i], end= " ")
    print()
    
if countpositive == 0:
            print ("-")
else:
    for i in range (n):
        if nnumbers [i] < 0:
            print (nnumbers [i], end= " ")
    print()

#Methods 2:
for i in range (n):
    if nnumbers [i] > 0:
        countpositive += 1  
    elif nnumbers [i] < 0:
        countnegative += 1

print (countpositive, countnegative)
    
if countpositive == 0:
            print ("-")
else:
    for i in range (n):
        if nnumbers [i] > 0:
            print (nnumbers [i], end= " ")
    print()
    
if countpositive == 0:
            print ("-")
else:
    for i in range (n ):
        if nnumbers [i] < 0:
            print (nnumbers [i], end= " ")
    print()

#Approach2:
# positive = []
# negative = []

# for x in nnumbers:
#     if x > 0:
#         positive.append(x)
#     elif x < 0:
#         negative.append(x)

# print( len(positive), len(negative))
# print(*positive if positive else ["-"])
# print(*negative if negative else ["-"])