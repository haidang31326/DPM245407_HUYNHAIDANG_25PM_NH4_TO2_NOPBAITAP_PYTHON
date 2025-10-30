import math

def tinh_tong_uoc_so(n):
 

    if n <= 1:
        return 0

    tong = 1 
    
    
    sqrt_n = int(math.sqrt(n))
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
           
            tong += i
           
            if i * i != n:
                tong += n // i
    
    return tong


def kiem_tra_so_hoan_thien(n):
  
    if n <= 0:
        return False
    return tinh_tong_uoc_so(n) == n


def kiem_tra_so_thinh_vuong(n):
   
    if n <= 0:
        return False
    return tinh_tong_uoc_so(n) > n


if __name__ == "__main__":
    print("--- CHƯƠNG TRÌNH KIỂM TRA SỐ HOÀN THIỆN VÀ SỐ THỊNH VƯỢNG ---")
    
    try:
        
        so_can_kiem_tra = int(input("Nhập vào một số nguyên dương để kiểm tra: "))

        if so_can_kiem_tra <= 0:
            print("Vui lòng nhập một số lớn hơn 0.")
        else:
           
            print("-" * 30)
            if kiem_tra_so_hoan_thien(so_can_kiem_tra):
                print(f" {so_can_kiem_tra} là một SỐ HOÀN THIỆN.")
            elif kiem_tra_so_thinh_vuong(so_can_kiem_tra):
                print(f" {so_can_kiem_tra} là một SỐ THỊNH VƯỢNG.")
            else:
                
                print(f"ℹ️ {so_can_kiem_tra} không phải là số hoàn thiện hay số thịnh vượng.")
                
    except ValueError:
        print("Lỗi: Dữ liệu nhập vào không hợp lệ. Vui lòng chỉ nhập số nguyên.")