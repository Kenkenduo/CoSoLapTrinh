so_KW = int(input("nhap so: "))

if so_KW <= 100:
    don_gia = 550
else:
    if so_KW <= 150:
        don_gia = 750
    else:
        if so_KW <= 200:
            don_gia = 950
        else:
            don_gia = 1350
thanh_tien = so_KW * don_gia * 1.1
print("Phải trả = ", thanh_tien)