'''Yêu cầu:
Nhập vào 1 tháng, xuất tháng đó có bao nhiêu ngày.
1,3,5,7,8,10,12➔31 ngày
4,6,9,11➔có 30 ngày
Nếu là tháng 2 thì yêu cầu nhập thêm năm. Năm nhuần thì tháng 2 có 29 ngày,
không nhuần có 28 ngày'''
print("Chuong trinh dem so ngay trong thang")
month = int (input("Nhao vao 1 thang (1-12): "))
if month in [1,3,5,7,8,10,12]:
    print("Thang", month, "co 31 ngay")
else:
    if month in(4,6,9,11):
        print("Thang", month, "co 30 ngay")
    else:
        if month == 2:
            year = int(input("nhap vao nam: "))
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                print("Thang 2 nam", year, "co 29 ngay")
            else:
                print("Thang 2 nam", year, "co 28 ngay")
        else:
            print("Khong hop le vui long nhap lai thang (1-12)")



