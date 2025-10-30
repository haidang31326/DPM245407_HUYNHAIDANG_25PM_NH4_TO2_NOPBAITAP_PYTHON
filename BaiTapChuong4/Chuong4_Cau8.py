# Import thư viện math để sử dụng các hàm toán học
import math

def tinh_logarit():
  
    print("--- CHƯƠNG TRÌNH TÍNH LOGARIT ---")

    try:
        x = float(input("Nhập vào số x (lưu ý: x phải > 0): "))

        if x <= 0:
            print("Lỗi: Số x phải lớn hơn 0. Vui lòng chạy lại chương trình.")
            return
    except ValueError:
        print("Lỗi: Dữ liệu nhập vào không phải là một số. Vui lòng chạy lại chương trình.")
        return

    
    print("\nChọn loại logarit bạn muốn tính:")
    print("1. Logarit tự nhiên (ln(x))")
    print("2. Logarit thập phân (log cơ số 10)")
    print("3. Logarit với cơ số bất kỳ")

    choice = input("Lựa chọn của bạn (nhập 1, 2, hoặc 3): ")


    if choice == '1':
        ket_qua = math.log(x)
        print(f"Logarit tự nhiên của {x} là: ln({x}) = {ket_qua}")
    elif choice == '2':
        ket_qua = math.log10(x)
        print(f"Logarit thập phân của {x} là: log({x}) = {ket_qua}")
    elif choice == '3':
        try:
            # Yêu cầu nhập cơ số b
            b = float(input("Nhập vào cơ số b (lưu ý: b > 0 và b != 1): "))
            # Kiểm tra điều kiện của cơ số
            if b <= 0 or b == 1:
                print("Lỗi: Cơ số b phải lớn hơn 0 và khác 1.")
            else:
                ket_qua = math.log(x, b)
                print(f"Logarit cơ số {b} của {x} là: {ket_qua}")
        except ValueError:
            print("Lỗi: Cơ số nhập vào không phải là một số.")
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn 1, 2, hoặc 3.")


tinh_logarit()