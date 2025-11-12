import tkinter as tk

def convert_f_to_c():
    """Lấy giá trị độ F từ ô nhập, tính toán và hiển thị độ C."""
    try:
        # Lấy giá trị từ ô nhập
        f_value_str = entry_f.get()
        if not f_value_str:
            lbl_ketqua.config(text="Chưa nhập!", fg="red")
            return

        f_value = float(f_value_str)
        
        # Công thức chuyển đổi: C = (F - 32) * 5/9
        c_value = (f_value - 32) * 5 / 9
        
        # Hiển thị kết quả, làm tròn 2 chữ số thập phân
        lbl_ketqua.config(text=f"{c_value:.2f}", fg="black")
        
    except ValueError:
        # Bắt lỗi nếu người dùng nhập không phải là số
        lbl_ketqua.config(text="Không hợp lệ!", fg="red")

# --- Cài đặt giao diện (GUI) ---

# 1. Tạo cửa sổ chính
window = tk.Tk()
window.title("Chuyển đổi F sang C")
window.resizable(False, False)

# 2. Tạo một Frame (khung) chính màu vàng
main_frame = tk.Frame(
    window, 
    bg="yellow", 
    padx=20, 
    pady=20, 
    highlightbackground="blue", 
    highlightthickness=2
)
main_frame.pack(padx=10, pady=10)

# 3. Tạo các thành phần bên trong Frame
# Hàng 0: Nhập độ F và ô nhập liệu
lbl_nhap = tk.Label(
    main_frame, 
    text="Nhập độ F", 
    bg="yellow", 
    font=("Arial", 12)
)
lbl_nhap.grid(row=0, column=0, padx=5, pady=10, sticky="e")

entry_f = tk.Entry(
    main_frame, 
    width=15, 
    font=("Arial", 12, "bold"), 
    fg="red", 
    justify="center"
)
entry_f.grid(row=0, column=1, padx=5, pady=10)
entry_f.insert(0, "350") # Thêm giá trị 350 như trong ảnh

# Hàng 1: Nút Chuyển
btn_chuyen = tk.Button(
    main_frame, 
    text="Chuyển", 
    font=("Arial", 11, "bold"), 
    width=10, 
    command=convert_f_to_c,
    bg="lightblue"
)
btn_chuyen.grid(row=1, column=1, pady=10)

# Hàng 2: Nhãn Độ C và Kết quả
lbl_c = tk.Label(
    main_frame, 
    text="Độ C", 
    bg="yellow", 
    font=("Arial", 12)
)
lbl_c.grid(row=2, column=0, padx=5, pady=10, sticky="e")

lbl_ketqua = tk.Label(
    main_frame, 
    text="Độ C ở đây", 
    bg="yellow", 
    font=("Arial", 12, "bold"),
    width=15
)
lbl_ketqua.grid(row=2, column=1, padx=5, pady=10, sticky="w")

# 4. Chạy vòng lặp chính của ứng dụng
window.mainloop()