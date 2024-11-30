import tkinter as tk

root = tk.Tk()
# root.geometry('300x200')
root.resizable(False, False)
root.overrideredirect(False)

close_icon = tk.PhotoImage(file='./Assets/x_icon_2.png')
minimize_icon = tk.PhotoImage(file='./Assets/minimize_icon_background.png')

def close_panchang_window() :
    root.destroy()

def panchang_window() :
    root.title("Panchang")
    # root.overrideredirect(True)
    root.wm_attributes("-topmost", True)

    label = tk.Label(root, text="Panchang Here", font=("Arial", 15))
    label.pack(padx=10, pady=10)

    root.mainloop()