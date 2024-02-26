def tinh_so_ngay_trong_thang(nam, thang):
    if thang == 2:
        if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
            return 29  # Năm nhuận
        else:
            return 28  # Năm không nhuận
    elif thang in [4, 6, 9, 11]:
        return 30
    else:
        return 31

nam = int(input("Nhập năm: "))
thang = int(input("Nhập tháng: "))

so_ngay = tinh_so_ngay_trong_thang(nam, thang)
print("Số ngày trong tháng là:", so_ngay)