'''  Nhập vào 1 tháng, xuất ra tháng đó thuộc quý mấy trong năm.'''
import math
print("Chuong trinh xac dinh quy cua thang")
while True:
        month = int(input("Nhap vao so thang (1-12): "))
        if 1 <= month <= 12:
            break
        else:
            print("So thang khong hop le, vui long nhap lai!")


if month >=1 and month <=3:
        print("Thang", month,"thuoc quy 1")
elif month >=4 and month <=6:
        print("Thang", month, "thuoc quy 2")
elif month >=7 and month <=9:
        print("Thang", month, "thuoc quy 3")
elif month >=10 and month <=12:
        print("Thang", month, "thuoc quy 4")
    




