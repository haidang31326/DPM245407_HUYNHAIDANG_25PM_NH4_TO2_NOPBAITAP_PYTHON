import tkinter as tk
from tkinter import messagebox



def on_ok_click():
    """
    Hàm này được gọi khi nhấn nút OK.
    Nó sẽ lấy dữ liệu từ các ô nhập và kiểm tra.
    """
    old_pass = entry_old.get()
    new_pass = entry_new.get()
    confirm_pass = entry_confirm.get()


    if not old_pass or not new_pass or not confirm_pass:
        messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin.")

    elif new_pass != confirm_pass:
        messagebox.showerror("Lỗi", "Mật khẩu mới không khớp.")
    else:
 
        print(f"Kiểm tra: Old='{old_pass}', New='{new_pass}'")
        

        messagebox.showinfo("Thành công", "Đã thay đổi mật khẩu thành công!")
       
        window.destroy()

def on_cancel_click():
    """Đóng cửa sổ khi nhấn nút Cancel."""
    window.destroy()


window = tk.Tk()
window.title("Enter New Password")
window.resizable(False, False) 


main_frame = tk.Frame(window, padx=15, pady=15)
main_frame.pack()

font_style = ("Arial", 10)



entry_old = tk.Entry(main_frame, show="*", width=30, font=font_style)
entry_old.grid(row=0, column=1, padx=5, pady=5)


lbl_new = tk.Label(main_frame, text="New Password:", font=font_style)
lbl_new.grid(row=1, column=0, sticky="w", pady=5)

entry_new = tk.Entry(main_frame, show="*", width=30, font=font_style)
entry_new.grid(row=1, column=1, padx=5, pady=5)

lbl_confirm = tk.Label(main_frame, text="Enter New Password Again:", font=font_style)
lbl_confirm.grid(row=2, column=0, sticky="w", pady=5)

entry_confirm = tk.Entry(main_frame, show="*", width=30, font=font_style)
entry_confirm.grid(row=2, column=1, padx=5, pady=5)


button_frame = tk.Frame(main_frame)

button_frame.grid(row=3, column=0, columnspan=2, pady=10)

btn_ok = tk.Button(button_frame, text="OK", width=10, command=on_ok_click)
btn_ok.pack(side="left", padx=10)

btn_cancel = tk.Button(button_frame, text="Cancel", width=10, command=on_cancel_click)
btn_cancel.pack(side="left", padx=10)


window.mainloop()