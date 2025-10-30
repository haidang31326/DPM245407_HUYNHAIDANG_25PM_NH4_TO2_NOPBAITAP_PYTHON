''' Viết chương trình nhập vào một số, kiểm tra xem số này có phải là số nguyên tố 
hay không. Hỏi người dùng có tiếp tục sử dụng hay thoát phần mềm. (Số nguyên tố là số lớn hơn 1 và chỉ chia hết cho 1 và chính nó)'''
import math

n = int(input("Nhap mot so nguyen: "))

if n <= 1:
    print(n, "khong phai la so nguyen to")
else:
    is_prime = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print(n, "la so nguyen to")
    else:
        print(n, "khong phai la so nguyen to")





