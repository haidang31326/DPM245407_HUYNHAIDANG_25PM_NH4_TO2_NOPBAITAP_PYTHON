# Giai cau 3
''' Yêu cầu:
Viết chương trình nhập vào điểm ba môn Toán, Lý, Hóa của một học sinh. In ra
điểm trung bình của học sinh đó với hai số lẻ thập phân.'''
import math
toan=float(input("Nhập điểm Toán:"))
ly=float(input("Nhập điểm lý:"))
hoa=float(input("Nhập điểm hóa:"))
while (toan >= 10 or ly >= 10 or hoa >= 10):
        print("Điểm nhập vào phải nhỏ hơn hoặc bằng 10. Vui lòng nhập lại.\n")
        toan=float(input("Nhập điểm Toán:"))
        ly=float(input("Nhập điểm lý:"))
        hoa=float(input("Nhập điểm hóa:"))
        
dtb=(toan+ly+hoa)/3
print("Điểm trung bình=",dtb)
print("Điểm lam tron=",round(dtb,2))
           
     


