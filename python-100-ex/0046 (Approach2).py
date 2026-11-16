n, x = map(int, (input().split()))
nnumbers = list(map( int, input().split()))

if len(nnumbers) != n:
    print("Nhap sai so luong phan tu")
    exit()
for i in range (len(nnumbers)):
    if nnumbers [i] == x:
        print ("Yes")
        print (i)
        break

else:
    print ("No")

#Methods 2:
#found = False

#for i in range (len(nnumbers)):
 #   if nnumbers [i] == x:
  #      print ("Yes\n" + str (i))
   #     found = True
    #    break

#if not found:
 #   print ("No")



#Approach2:
#if x in nnumbers:
#    print("Yes\n" + str( nnumbers.index(x)))
#else:
 #   print("No")

#Methods2:
#if x in nnumbers:
 #   print("Yes")
  #  print( nnumbers.index(x))
#else:
 #   print("No")
