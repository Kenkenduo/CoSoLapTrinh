gia_niem_yet = float(input("Nhap Gia Niem Yet: "))
chiet_khau = float(input("Nhap Chiet Khau: "))
vat = (gia_niem_yet - chiet_khau) * 0.01
gia_ban = gia_niem_yet - chiet_khau + vat
print(f"Gia Ban: {gia_ban} ")