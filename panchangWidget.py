import tkinter as tk

root = tk.Tk()

def close_panchang_window() :
    root.destroy()

def panchang_window() :
    root.title("Panchang")
    root.overrideredirect(True)
    root.wm_attributes("-topmost", True)

    label = tk.Label(root, text="Panchang Here", font=("Arial", 24))
    label.pack(padx=20, pady=20)

    close_button = tk.Button(root, text="Close", command=close_panchang_window, font=("Arial", 12))
    close_button.pack(pady=10)

    root.mainloop()