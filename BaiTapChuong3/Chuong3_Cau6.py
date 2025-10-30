''' Nhập một số n có tối đa 2 chữ số. Hãy cho biết cách đọc ra dạng chữ.
(vd: n=35 => Ba mươi lăm, n=5 => năm). '''
import math
print("Chuong trinh doc so toi da 2 chu so")
n = int(input("Nhap vao so n (0<=100):"))
if n < 0 or n > 99:
    print("So khong hop le vui long nhap lai")
else:
    if n < 10:
        donvi = n
        if donvi == 0:
            print("Khong")
        elif donvi == 1:
            print("Mot")
        elif donvi == 2:
            print("Hai")
        elif donvi == 3:
            print("Ba")
        elif donvi == 4:
            print("Bon")
        elif donvi == 5:
            print("Nam")
        elif donvi == 6:
            print("Sau")
        elif donvi == 7:
            print("Bay")
        elif donvi == 8:
            print("Tam")
        else:
            print("Chin")
    else:
        chuc = n // 10
        donvi = n % 10
        if chuc == 1:
            chuSoChuc = "Muoi"
        elif chuc == 2:
            chuSoChuc = "Hai muoi"
        elif chuc == 3:
            chuSoChuc = "Ba muoi"
        elif chuc == 4:
            chuSoChuc = "Bon muoi"
        elif chuc == 5:
            chuSoChuc = "Nam muoi"
        elif chuc == 6:
            chuSoChuc = "Sau muoi"
        elif chuc == 7:
            chuSoChuc = "Bay muoi"
        elif chuc == 8:
            chuSoChuc = "Tam muoi"
        else:
            chuSoChuc = "Chin muoi"
        
        if donvi == 0:
            chuSoDonVi = ""
        elif donvi == 1:
            chuSoDonVi = " mot"
        elif donvi == 2:
            chuSoDonVi = " hai"
        elif donvi == 3:
            chuSoDonVi = " ba"
        elif donvi == 4:
            chuSoDonVi = " bon"
        elif donvi == 5:
            chuSoDonVi = " lam"
        elif donvi == 6:
            chuSoDonVi = " sau"
        elif donvi == 7:
            chuSoDonVi = " bay"
        elif donvi == 8:
            chuSoDonVi = " tam"
        else:
            chuSoDonVi = " chin"
        
print(chuSoChuc + chuSoDonVi)



        
        




