import tkinter as tk

def convert_to_lunar(year):
    THIEN_CAN = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]
    DIA_CHI = ["Thân", "Dậu", "Tuất", "Hợi", "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi"]
    
    can = THIEN_CAN[year % 10]
    chi = DIA_CHI[year % 12]
    
    return f"{can} {chi}"

def handle_convert():
    try:
        year_str = entry_year.get()
        if not year_str:
            lbl_ketqua.config(text="Chưa nhập!", fg="red")
            return
        
        year_int = int(year_str)
        lunar_year = convert_to_lunar(year_int)
        lbl_ketqua.config(text=lunar_year, fg="black")
        
    except ValueError:
        lbl_ketqua.config(text="Năm không hợp lệ!", fg="red")

window = tk.Tk()
window.title("Chuyển đổi Âm lịch")
window.resizable(False, False)

main_frame = tk.Frame(
    window, 
    bg="yellow", 
    padx=20, 
    pady=20, 
    highlightbackground="blue", 
    highlightthickness=2
)
main_frame.pack(padx=10, pady=10)

lbl_nhap = tk.Label(
    main_frame, 
    text="Nhập năm dương:", 
    bg="yellow", 
    font=("Arial", 12)
)
lbl_nhap.grid(row=0, column=0, padx=5, pady=10, sticky="e")

entry_year = tk.Entry(
    main_frame, 
    width=15, 
    font=("Arial", 12, "bold"), 
    fg="red", 
    justify="center"
)
entry_year.grid(row=0, column=1, padx=5, pady=10)
entry_year.insert(0, "1982")

btn_chuyen = tk.Button(
    main_frame, 
    text="Chuyển", 
    font=("Arial", 11, "bold"), 
    width=10, 
    command=handle_convert,
    bg="lightblue"
)
btn_chuyen.grid(row=1, column=1, pady=10)

lbl_am = tk.Label(
    main_frame, 
    text="Năm âm:", 
    bg="yellow", 
    font=("Arial", 12)
)
lbl_am.grid(row=2, column=0, padx=5, pady=10, sticky="e")

lbl_ketqua = tk.Label(
    main_frame, 
    text="", 
    bg="yellow", 
    font=("Arial", 12, "bold")
)
lbl_ketqua.grid(row=2, column=1, padx=5, pady=10, sticky="w")

window.mainloop()