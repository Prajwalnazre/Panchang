import tkinter as tk

root = tk.Tk()
# root.geometry('300x200')
root.resizable(False, False)
root.overrideredirect(False)

# close_icon = tk.PhotoImage(file='./Assets/x_icon_2.png')
# minimize_icon = tk.PhotoImage(file='./Assets/minimize_icon_background.png')

frame = tk.Frame(root)
frame.pack(pady=20)

def panchang_window(panchang_object) :
    root.title("Panchang")
    # root.overrideredirect(True)
    # root.wm_attributes("-topmost", True)

    main_label = tk.Label(frame, text="Hindu Panchang", font=("Arial", 15))
    main_label.pack(padx=10, pady=10)
    panchang_object.printPanchangInfo()
    label_texts = [f"MAASA : {panchang_object.maasa}", f"THITHI : {panchang_object.thithi}", f"PAKSHA : {panchang_object.paksha}", f"DAY OF THE MONTH : {panchang_object.dayOfMonth}"]
    for text in label_texts :
        label = tk.Label(frame, text=text)
        label.pack(padx=5, pady=5)

    root.mainloop()