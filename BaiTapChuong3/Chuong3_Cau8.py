''' Nhập vào một ngày (ngày, tháng, năm). Tìm ngày kế sau ngày  
vừa nhập (ngày/tháng/năm).'''
import math
a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))
x = str(input("Chon 1 trong 4 phep tinh (+,-,*,/): "))

if x=="+":
    print("Ket qua:",a+b)
elif x=="-":
    print("Ket qua:",a-b)
elif x=="*":
    print("Ket qua:",a*b)
elif x=="/":  
  if b==0:
        print("Khong the chia cho 0")
  else:
        print("Ket qua:",a/b)

