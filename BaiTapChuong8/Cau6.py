import tkinter as tk

window = tk.Tk()
window.title("frame 2") 
window.resizable(False, False)


styles = ["raised", "sunken", "flat", "ridge", "groove", "solid"]
borders = [0, 1, 2, 3, 4]




tk.Label(window, text="", width=15).grid(row=0, column=0, padx=5, pady=5)

for col_index, style in enumerate(styles):

    header_label = tk.Label(window, text=style, width=10, font=("Arial", 10, "bold"))
    header_label.grid(row=0, column=col_index + 1, padx=5, pady=5)



for row_index, bw in enumerate(borders):
    

    row_label = tk.Label(window, text=f"borderwidth = {bw}", width=15)
    row_label.grid(row=row_index + 1, column=0, padx=5, pady=5)
    

    for col_index, style in enumerate(styles):
        

        button = tk.Button(
            window, 
            text=style, 
            width=8,
  
            relief=style, 
            borderwidth=bw 
        )
        

        button.grid(row=row_index + 1, column=col_index + 1, padx=5, pady=5)



window.mainloop()