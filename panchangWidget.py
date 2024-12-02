import tkinter as tk
from datetime import date
from tkinter.font import Font
from PIL import ImageFont

root = tk.Tk()
# root.geometry('300x200')
root.resizable(False, False)
root.overrideredirect(False)

today = date.today()
akasha_font_path = 'AkashaRegular-Rprn6.ttf'
akasha_font_pil_font = ImageFont.truetype(akasha_font_path, size=17)
akasha_font = Font(family=akasha_font_pil_font.font.family, size=17)
# close_icon = tk.PhotoImage(file='./Assets/x_icon_2.png')
# minimize_icon = tk.PhotoImage(file='./Assets/minimize_icon_background.png')

# frame = tk.Frame(root)
# frame.pack(pady=20)

def panchang_window(panchang_object) :
    root.title("Panchang")
    # root.overrideredirect(True)
    # root.wm_attributes("-topmost", True)
    root.configure(bg="lightblue")
    today_upper_case = str(today.strftime('%B %d, %Y'))
    print(akasha_font)
    main_label = tk.Label(root, bg = "lightyellow", text=f"TODAY - {today_upper_case.upper()}", font=akasha_font)
    main_label.grid(row=0, columnspan=2, padx=10, pady=8, sticky="nsew")
    panchang_object.printPanchangInfo()
    label_texts = [
        f"MAASA : {panchang_object.maasa}",
        f"THITHI : {panchang_object.thithi}",
        f"PAKSHA : {panchang_object.paksha}",
        f"DAY OF THE MONTH : {panchang_object.dayOfMonth}"
    ]

    maasa_label = tk.Label(root, text = label_texts[0], bg="lightblue", font=akasha_font)
    thithi_label = tk.Label(root, text=label_texts[1], bg="lightblue", font=akasha_font)
    paksha_label = tk.Label(root, text=label_texts[2], bg="lightblue", font=akasha_font)
    day_of_the_month_label = tk.Label(root, text=label_texts[3], bg="lightblue", font=akasha_font)

    maasa_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
    day_of_the_month_label.grid(row=1, column=1,padx=10, pady=5, sticky=tk.W)
    thithi_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
    paksha_label.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    root.mainloop()