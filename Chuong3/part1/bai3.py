kw=int(input("Tieu thu="))
if kw <= 100:
    gia = 550
elif kw <= 150:
    gia = 750
elif kw <= 200:
    gia = 950
else:
    gia = 1350
    
tien = kw*gia*1.1

print("Phai tra=",tien)
