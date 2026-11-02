sumgiay = int(input())
h = sumgiay // 3600
m = sumgiay % 3600 // 60
s = sumgiay % 60
print(f"{h}:{m}:{s}")
