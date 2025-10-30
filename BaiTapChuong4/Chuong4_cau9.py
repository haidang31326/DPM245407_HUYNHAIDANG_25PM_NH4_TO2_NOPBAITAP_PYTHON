# Import thư viện math để sử dụng hàm tính căn bậc hai (sqrt)
import math

def tinh_can_long_vong_lap(n):
   
    if n < 1:
        return 0

    ket_qua = 1.0


    for i in range(2, n + 1):
        ket_qua = math.sqrt(i + ket_qua)
    
    return ket_qua

def tinh_can_long_de_quy(n):
    """
    Tính biểu thức căn lồng nhau bằng phương pháp đệ quy.
    S(n) = sqrt(n + S(n-1))
    """

    if n < 1:
        return 0
        
   
    if n == 1:
        return 1.0
    
    
    return math.sqrt(n + tinh_can_long_de_quy(n - 1))


if __name__ == "__main__":
    print("--- CHƯƠNG TRÌNH TÍNH CĂN BẬC HAI LỒNG NHAU ---")
    print("Công thức: S(n) = sqrt(n + sqrt(n-1 + ... + sqrt(1)))")

    try:
       
        n = int(input("Nhập vào số nguyên dương n: "))

        if n <= 0:
            print("Lỗi: Vui lòng nhập một số nguyên dương.")
        else:
           
            ket_qua_lap = tinh_can_long_vong_lap(n)
            print(f"🔄 Kết quả tính bằng vòng lặp: S({n}) = {ket_qua_lap}")

            ket_qua_de_quy = tinh_can_long_de_quy(n)
            print(f"🔁 Kết quả tính bằng đệ quy:   S({n}) = {ket_qua_de_quy}")

    except ValueError:
        print("Lỗi: Dữ liệu nhập vào không phải là số nguyên. Vui lòng chạy lại.")