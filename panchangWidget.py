import tkinter as tk
from datetime import date

root = tk.Tk()
# root.geometry('300x200')
root.resizable(False, False)
root.overrideredirect(False)

today = date.today()

# close_icon = tk.PhotoImage(file='./Assets/x_icon_2.png')
# minimize_icon = tk.PhotoImage(file='./Assets/minimize_icon_background.png')

# frame = tk.Frame(root)
# frame.pack(pady=20)

def panchang_window(panchang_object) :
    root.title("Panchang")
    # root.overrideredirect(True)
    # root.wm_attributes("-topmost", True)

    main_label = tk.Label(root, text=f"Today - {today.strftime('%B %d, %Y')}", font=("Arial", 12))
    main_label.grid(row=0, columnspan=2, padx=10, pady=5, sticky="nsew")
    panchang_object.printPanchangInfo()
    label_texts = [
        f"MAASA : {panchang_object.maasa}",
        f"THITHI : {panchang_object.thithi}",
        f"PAKSHA : {panchang_object.paksha}",
        f"DAY OF THE MONTH : {panchang_object.dayOfMonth}"
    ]

    maasa_label = tk.Label(root, text = label_texts[0])
    thithi_label = tk.Label(root, text=label_texts[1])
    paksha_label = tk.Label(root, text=label_texts[2])
    day_of_the_month_label = tk.Label(root, text=label_texts[3])

    maasa_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
    day_of_the_month_label.grid(row=1, column=1,padx=5, pady=5)

    thithi_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
    paksha_label.grid(row=2, column=1, padx=5, pady=5)

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    root.mainloop()