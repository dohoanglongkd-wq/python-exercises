n = int(input())
#Study-flag-variable
snt = True
for i in range (2, n):
    if n % i == 0:
        snt = False
        break
if snt:
    print ("Yes") 
elif n <= 1:
    print("No")
else:
    print("No")
