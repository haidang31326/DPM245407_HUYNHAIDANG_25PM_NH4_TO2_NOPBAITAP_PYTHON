import tkinter as tk

def calculate_bmi():
    try:
        height_str = entry_height.get()
        weight_str = entry_weight.get()
        
        if not height_str or not weight_str:
            bmi_var.set("Lỗi")
            status_var.set("Lỗi")
            risk_var.set("Lỗi")
            return

        height = float(height_str)
        weight = float(weight_str)

        if height <= 0:
            bmi_var.set("Lỗi chia 0")
            status_var.set("")
            risk_var.set("")
            return

        bmi = weight / (height * height)
        bmi_var.set(f"{bmi:.2f}")

        status = ""
        risk = ""

        if bmi < 18.5:
            status = "Gầy"
            risk = "Nguy cơ thấp"
        elif 18.5 <= bmi < 25:
            status = "Bình thường"
            risk = "Nguy cơ trung bình"
        elif 25 <= bmi < 30:
            status = "Hơi béo"
            risk = "Hơi hơi cao"
        elif 30 <= bmi < 35:
            status = "Béo phì độ 1"
            risk = "Nguy cơ cao"
        else:
            status = "Béo phì độ 2+"
            risk = "Nguy cơ rất cao"

        status_var.set(status)
        risk_var.set(risk)

    except ValueError:
        bmi_var.set("Nhập sai")
        status_var.set("Nhập sai")
        risk_var.set("Nhập sai")

def exit_app():
    window.destroy()

window = tk.Tk()
window.title("Tính BMI")
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

font_style = ("Arial", 11)
entry_width = 22

lbl_height = tk.Label(main_frame, text="Nhập chiều cao:", bg="yellow", font=font_style)
lbl_height.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_height = tk.Entry(main_frame, width=entry_width, font=font_style, fg="red", justify="center")
entry_height.grid(row=0, column=1, padx=10, pady=10)
entry_height.insert(0, "1.8")

lbl_weight = tk.Label(main_frame, text="Nhập cân nặng", bg="yellow", font=font_style)
lbl_weight.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_weight = tk.Entry(main_frame, width=entry_width, font=font_style, fg="red", justify="center")
entry_weight.grid(row=1, column=1, padx=10, pady=10)
entry_weight.insert(0, "172")

btn_calc = tk.Button(
    main_frame, 
    text="Tính BMI", 
    font=font_style, 
    command=calculate_bmi,
    bg="lightblue"
)
btn_calc.grid(row=2, column=1, pady=10, sticky="ew")

lbl_bmi = tk.Label(main_frame, text="BMI của bạn:", bg="yellow", font=font_style)
lbl_bmi.grid(row=3, column=0, padx=10, pady=10, sticky="w")

bmi_var = tk.StringVar(value="x")
entry_bmi = tk.Entry(
    main_frame, 
    textvariable=bmi_var, 
    width=entry_width, 
    font=font_style, 
    state="readonly", 
    readonlybackground="white", 
    justify="center"
)
entry_bmi.grid(row=3, column=1, padx=10, pady=10)

lbl_status = tk.Label(main_frame, text="Tình trạng của bạn", bg="yellow", font=font_style)
lbl_status.grid(row=4, column=0, padx=10, pady=10, sticky="w")

status_var = tk.StringVar(value="Hơi Béo")
entry_status = tk.Entry(
    main_frame, 
    textvariable=status_var, 
    width=entry_width, 
    font=(font_style[0], font_style[1], "bold"),
    state="readonly", 
    readonlybackground="white", 
    fg="red", 
    justify="center"
)
entry_status.grid(row=4, column=1, padx=10, pady=10)

lbl_risk = tk.Label(main_frame, text="Nguy cơ phát triển bệnh", bg="yellow", font=font_style)
lbl_risk.grid(row=5, column=0, padx=10, pady=10, sticky="w")

risk_var = tk.StringVar(value="Hơi hơi cao")
entry_risk = tk.Entry(
    main_frame, 
    textvariable=risk_var, 
    width=entry_width, 
    font=(font_style[0], font_style[1], "bold"),
    state="readonly", 
    readonlybackground="white", 
    fg="red", 
    justify="center"
)
entry_risk.grid(row=5, column=1, padx=10, pady=10)

btn_exit = tk.Button(
    main_frame, 
    text="Thoát", 
    font=font_style, 
    command=exit_app,
    bg="lightblue"
)
btn_exit.grid(row=6, column=1, pady=10, sticky="ew")

window.mainloop()