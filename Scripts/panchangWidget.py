'''
Functions :
>> panchang_window(panchang_object)
- Create UI using Tkinter
- Used in main.py
'''

import tkinter as tk
from tkinter import ttk
from datetime import date
from tkinter.font import Font
from PIL import ImageFont

root = tk.Tk()
# root.geometry('300x200')
root.resizable(False, False)

# Remove the default close button
root.overrideredirect(False) 

today = date.today()
akasha_font_path = 'AkashaRegular-Rprn6.ttf'
akasha_font_pil_font = ImageFont.truetype(akasha_font_path, size=17)
akasha_font = Font(family=akasha_font_pil_font.font.family, size=17)

final_font = akasha_font

# close_icon = tk.PhotoImage(file='./Assets/x_icon_2.png')
# minimize_icon = tk.PhotoImage(file='./Assets/minimize_icon_background.png')

# frame = tk.Frame(root)
# frame.pack(pady=20)

def panchang_window(panchang_object) :
    root.title("Panchang")
    # root.overrideredirect(True)
    # root.wm_attributes("-topmost", True)
    root.configure(bg="#fdb563")
    today_upper_case = str(today.strftime('%B %d, %Y'))
    # print(akasha_font)

    button_frame = tk.Frame(root, bg="#fdb563")
    button_frame.grid(row=0, column=0, columnspan=2,  sticky="ew", padx=0, pady=0)

    # minimize_button = ttk.Button(button_frame, text="_", command=minimize_window, width=4, style="Custom.TButton")
    
    minimize_button = tk.Button(button_frame, text="__", command=minimize_window, width=4, bg="#fdb563", bd=0, highlightthickness=0)
    minimize_button.pack(side=tk.RIGHT, padx=5)

    # close_button = ttk.Button(button_frame, text="x", command=close_window, width=4, style="Custom.TButton")
    
    close_button = tk.Button(button_frame, text="x", command=close_window, width=4, bg="#fdb563", bd=0, highlightthickness=0, font='Helvectica')
    close_button.pack(side=tk.RIGHT, padx=0)

    main_label = tk.Label(root, bg = "lightyellow", text=f"TODAY - {today_upper_case.upper()}", font=final_font)
    main_label.grid(row=1, columnspan=2, padx=10, pady=8, sticky="nsew")
    panchang_object.printPanchangInfo()
    label_texts = [
        f"MAASA : {panchang_object.maasa}",
        f"THITHI : {panchang_object.thithi}",
        f"PAKSHA : {panchang_object.paksha}",
        f"DAY OF THE MONTH : {panchang_object.dayOfMonth}"
    ]

    maasa_label = tk.Label(root, text = label_texts[0], bg="#fdb563", font=final_font)
    thithi_label = tk.Label(root, text=label_texts[1], bg="#fdb563", font=final_font)
    paksha_label = tk.Label(root, text=label_texts[2], bg="#fdb563", font=final_font)
    day_of_the_month_label = tk.Label(root, text=label_texts[3], bg="#fdb563", font=final_font)

    maasa_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
    day_of_the_month_label.grid(row=2, column=1,padx=10, pady=5, sticky=tk.W)
    thithi_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
    paksha_label.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)

    root.grid_rowconfigure(0, weight=0, minsize=5)
    root.grid_rowconfigure(1, weight=3)
    root.grid_rowconfigure(2, weight=3)
    root.grid_rowconfigure(3, weight=3)

    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    root.mainloop()

def minimize_window() :
    root.iconify()

def close_window() :
    root.destroy()