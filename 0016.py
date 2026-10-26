TBHKI, TBHKII = map(float, input().split())
TBCN = (TBHKI + TBHKII * 2) / 3
print(f"{TBCN:.1f}")
if TBCN < 3.5:
    print("Kem")
elif TBCN < 5:
    print("Yeu")
elif TBCN < 6.5:
    print("Trung binh")
elif TBCN < 8:
    print("Kha")
else:
    print("Gioi")
