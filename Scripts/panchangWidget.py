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
from PIL import Image, ImageTk

root = tk.Tk()
# root.geometry('300x200')
root.resizable(False, False)

# Remove the default close button
root.overrideredirect(True) 

today = date.today()
akasha_font_path = 'AkashaRegular-Rprn6.ttf'
akasha_font_pil_font = ImageFont.truetype(akasha_font_path, size=17)
akasha_font = Font(family=akasha_font_pil_font.font.family, size=17)

final_font = akasha_font

# close_icon = tk.PhotoImage(file='./Assets/x_icon_2.png')
# minimize_icon = tk.PhotoImage(file='./Assets/minimize_icon_background.png')

# frame = tk.Frame(root)
# frame.pack(pady=20)

x_icon_image = Image.open("../Assets/x_icon_compressed.png")
x_icon_photo = ImageTk.PhotoImage(x_icon_image)

minimize_icon_image = Image.open("../Assets/minimize_icon_compressed.png")
minimize_icon_photo = ImageTk.PhotoImage(minimize_icon_image)

maximize_icon_image = Image.open("../Assets/maximize_icon_compressed.png")
maximize_icon_photo = ImageTk.PhotoImage(maximize_icon_image)

def panchang_window(panchang_object) :
    root.title("Panchang")
    # root.overrideredirect(True)
    # root.wm_attributes("-topmost", True)
    root.configure(bg="#fdb563")
    today_upper_case = str(today.strftime('%B %d, %Y'))
    # print(akasha_font)   

    main_label = tk.Label(root, bg = "lightyellow", text=f"TODAY - {today_upper_case.upper()}", font=final_font)
    
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

    button_frame = tk.Frame(root, bg="#fdb563")
    button_frame.grid(row=0, column=0, columnspan=2,  sticky="ew", padx=0, pady=0)
    button_frame.grid_remove()
    # minimize_button = ttk.Button(button_frame, text="_", command=minimize_window, width=4, style="Custom.TButton")
    
    close_button = tk.Button(
        button_frame,
        # height=2,
        # text="x",
        image=x_icon_photo, 
        command=close_window, 
        # width=4, 
        bg="#fdb563", 
        bd=0, 
        highlightthickness=1, 
        # font='Helvectica'
        )
    close_button.pack(side=tk.RIGHT, padx=5)

    maximize_button = tk.Button(
        button_frame, 
        # text="-", 
        image=maximize_icon_photo,
        command=lambda: maximize_window(main_label, maasa_label, thithi_label, paksha_label, day_of_the_month_label, maximize_button, minimize_button), 
        # width=4, 
        bg="#fdb563", 
        bd=0, 
        # height=2,
        highlightthickness=1,
        # font='Helvectica'
        )
    maximize_button.pack(side=tk.RIGHT, padx=5)
    maximize_button.pack_forget()

    minimize_button = tk.Button(
        button_frame, 
        # text="-", 
        image=minimize_icon_photo,
        command=lambda: minimize_window(main_label, maasa_label, thithi_label, paksha_label, day_of_the_month_label, maximize_button, minimize_button), 
        # width=4, 
        bg="#fdb563", 
        bd=0, 
        # height=2,
        highlightthickness=1,
        # font='Helvectica'
        )
    minimize_button.pack(side=tk.RIGHT, padx=5)

    # close_button = ttk.Button(button_frame, text="x", command=close_window, width=4, style="Custom.TButton")
    main_label.grid(row=1, columnspan=2, padx=10, pady=8, sticky="nsew")
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

    # root.bind("<Unmap>", restore_window)

    main_label.bind("<Enter>", lambda event: main_label_enter(event, button_frame))
    main_label.bind("<Leave>", lambda event: main_label_leave(event, button_frame))
    button_frame.bind("<Button-1>", start_move_widget)
    button_frame.bind("<B1-Motion>", stop_move_widget)

    root.mainloop()

def minimize_window(main_label, maasa_label, thithi_label, paksha_label, day_of_the_month_label, maximize_button, minimize_button) :
    print(minimize_button)
    print(maximize_button)
    # root.update_idletasks()
    # root.overrideredirect(False)  # Temporarily disable override
    # root.iconify()  # Minimize the window
    # root.after(5, lambda: root.overrideredirect(True))  # Reapply override when restored
    
    maasa_label.grid_remove()
    thithi_label.grid_remove()
    paksha_label.grid_remove()
    day_of_the_month_label.grid_remove()
    main_label.grid_remove()
    maximize_button.pack(side=tk.RIGHT, padx=5)
    minimize_button.pack_forget()
    print("Called Mini")

def maximize_window(main_label, maasa_label, thithi_label, paksha_label, day_of_the_month_label, maximize_button, minimize_button) :
    main_label.grid(row=1, columnspan=2, padx=10, pady=8, sticky="nsew")
    maasa_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
    day_of_the_month_label.grid(row=2, column=1,padx=10, pady=5, sticky=tk.W)
    thithi_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
    paksha_label.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)
    minimize_button.pack(side=tk.RIGHT, padx=5)
    maximize_button.pack_forget()
    print("Called Maxi")

def close_window() :
    root.destroy()

# def restore_window(event=None) :
#     print("Taam")
#     root.deiconify()
#     root.overrideredirect(True)
#     root.lift()
    
def main_label_enter(event, button_frame) :
    button_frame.hover = False
    button_frame.grid(row=0, column=0, columnspan=2,  sticky="ew", padx=0, pady=0)

def main_label_leave(event, button_frame) :
    button_frame.hover = True
    delay = 10000
    root.after(delay, lambda: remove_button_frame(button_frame))

def remove_button_frame(button_frame) :
    print(button_frame.hover)
    if button_frame.hover :
        button_frame.grid_remove()

def start_move_widget(event) :
    root.x = event.x
    root.y = event.y

def stop_move_widget(event) :
    x = event.x_root - root.x
    y = event.y_root - root.y
    root.geometry(f"+{x}+{y}")