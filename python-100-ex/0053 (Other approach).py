a = list(map( int, input().split()))
count = 0
snt_list = []

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
            count += 1
            snt_list.append(i)
                
if count == 0:
    print( "-")
else:
    print(max(snt_list))

# Approach2: No count
# for i in a:
#     snt = True

#     if i < 2:
#         snt = False
#     else:
#         for j in range (2, int( i ** 0.5) + 1):
#             if i % j == 0:
#                 snt = False
#                 break

#         if snt:
#             snt_list.append(i)

# if len( snt_list) == 0:
#     print( "-")
# else:
#     print( max( snt_list))

# Approach 3: 
# max_snt = None

# for i in a:
#     snt = True

#     if i < 2:
#         snt = False
#     else:
#         for j in range (2, int( i ** 0.5) + 1):
#             if i % j == 0:
#                 snt = False
#                 break

#         if snt and (max_snt is None or i > max_snt):
#                  max_snt = i

# if max_snt == None:
#     print( "-")
# else:
#     print( max_snt)