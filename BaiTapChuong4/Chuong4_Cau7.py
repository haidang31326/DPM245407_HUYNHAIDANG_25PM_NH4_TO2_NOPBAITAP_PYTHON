''' Nhập toạ độ 2 điểm A(xA,yA), B(xB,yB). Tính và xuất độ dài đoạn AB. '''
import math

xA = float(input("Nhap toa do x diem A: "))
yA = float(input("Nhap toa do y diem A: "))

xB = float(input("Nhap toa do x diem B: "))
yB = float(input("Nhap toa do y diem B: "))

dAB = math.sqrt((xA - xB)**2 + (yB - yA)**2)

print("Dien tich 2 diem =",dAB)
