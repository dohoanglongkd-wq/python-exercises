n, x = map(int, (input().split()))
nnumbers = list(map( int, input().split()))

if len(nnumbers) != n:
    print("Nhap sai so luong phan tu")
    exit()
#for i in range (len(nnumbers)):
 #   if nnumbers [i] == x:
  #      print (i)
   #     break

#Approach2:
if x in nnumbers:
    print("Yes\n" + str( nnumbers.index(x)))
else:
    print("No")

#Methods2:
if x in nnumbers:
    print("Yes")
    print( nnumbers.index(x))
else:
    print("No")
