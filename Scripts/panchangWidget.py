'''
Functions :
>> panchang_window()
- Create UI using Tkinter
- Used in main.py
>> minimize_window()
- Custom minimize functionality
- Used within panchang_window() for minimize_button
>> maximize_window()
- Custom maximize functionality
- Used within panchang_window() for maximize_button
>> close_window()
- Close the widget
- Used within panchang_window() for close_button
>> top_area_enter()
- Handle mouse enter event when it enters the top area
- Used within panchang_window() for binding main_label and button_frame with "<Enter>" event
>> top_area_leave()
- Handle mouse leave event when it enters the top area
- Used within panchang_window() for binding main_label and button_frame with "<Leave>" event
>> check_and_remove_button_frame()
- Remove the button frame if conditions are met
- Used within top_area_leave() to schedule the delayed action directly
>> remove_button_frame()
- Remove the customer button frame
- Used within check_and_remove_button_frame() after checking if the delay has passed the 10 second mark
>> start_move_widget()
- Custom drag and drop function to start the change
- Used within panchang_window() - binded to "<Button-1>" event
>> stop_move_widget()
- Custom drag and drop function to stop at final position
- Used within panchang_window() - binded to "<B1-Motion>" event 
'''

import tkinter as tk
from tkinter import ttk
from datetime import date
from tkinter.font import Font
from PIL import ImageFont
from PIL import Image, ImageTk
import time

# Initialize root window
root = tk.Tk()

# Disable window size changing functionality
root.resizable(False, False)

# Remove the default close button
root.overrideredirect(True) 

# Importing Akasha font
akasha_font_path = 'AkashaRegular-Rprn6.ttf'
akasha_font_pil_font = ImageFont.truetype(akasha_font_path, size=17)
akasha_font = Font(family=akasha_font_pil_font.font.family, size=17)


# Importing custom icons for close, minimize and maximize functionality
x_icon_image = Image.open("../Assets/x_icon_compressed.png")
x_icon_photo = ImageTk.PhotoImage(x_icon_image)
minimize_icon_image = Image.open("../Assets/minimize_icon_compressed.png")
minimize_icon_photo = ImageTk.PhotoImage(minimize_icon_image)
maximize_icon_image = Image.open("../Assets/maximize_icon_compressed.png")
maximize_icon_photo = ImageTk.PhotoImage(maximize_icon_image)

# Create the Main Widget
def panchang_window(panchang_object) :
    root.title("Panchang")
    root.configure(bg="#fdb563")

    # Main Label contains the current date
    today = date.today()
    today_upper_case = str(today.strftime('%B %d, %Y'))
    main_label = tk.Label(root, bg = "lightyellow", text=f"TODAY - {today_upper_case.upper()}", font=akasha_font)

    # Information display strings
    label_texts = [
        f"MAASA : {panchang_object.maasa}",
        f"THITHI : {panchang_object.thithi}",
        f"PAKSHA : {panchang_object.paksha}",
        f"DAY OF THE MONTH : {panchang_object.dayOfMonth}"
    ]

    # Information Labels creation
    maasa_label = tk.Label(root, text = label_texts[0], bg="#fdb563", font=akasha_font)
    thithi_label = tk.Label(root, text=label_texts[1], bg="#fdb563", font=akasha_font)
    paksha_label = tk.Label(root, text=label_texts[2], bg="#fdb563", font=akasha_font)
    day_of_the_month_label = tk.Label(root, text=label_texts[3], bg="#fdb563", font=akasha_font)

    # Creating a Tkinter Frame for custom header that contains minimize, maximize and close buttons
    button_frame = tk.Frame(root, bg="#fdb563")
    button_frame.grid(row=0, column=0, columnspan=2,  sticky="ew", padx=0, pady=0) # Adding Frame to Grid
    button_frame.grid_remove() # Hiding this frame as it is necessary only when the user hovers on Main Label
    
    # Creating all the 3 buttons
    close_button = tk.Button(
        button_frame,
        image=x_icon_photo, 
        command=close_window, 
        bg="#fdb563", 
        bd=0, 
        highlightthickness=1
        )
    close_button.pack(side=tk.RIGHT, padx=5)

    maximize_button = tk.Button(
        button_frame, 
        image=maximize_icon_photo,
        command=lambda: maximize_window(
            main_label, 
            maasa_label, 
            thithi_label, 
            paksha_label, 
            day_of_the_month_label, 
            maximize_button, 
            minimize_button
            ), 
        bg="#fdb563", 
        bd=0, 
        highlightthickness=1,
        )
    maximize_button.pack(side=tk.RIGHT, padx=5)
    maximize_button.pack_forget() # Hiding this button during intialization - Appears only after being minimized

    minimize_button = tk.Button(
        button_frame, 
        image=minimize_icon_photo,
        command=lambda: minimize_window(
            main_label, 
            maasa_label, 
            thithi_label, 
            paksha_label, 
            day_of_the_month_label, 
            maximize_button, 
            minimize_button
            ), 
        bg="#fdb563", 
        bd=0, 
        highlightthickness=1,
        )
    minimize_button.pack(side=tk.RIGHT, padx=5)

    # Adding all the 5 created labels to Grid
    main_label.grid(row=1, columnspan=2, padx=10, pady=8, sticky="nsew")
    maasa_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
    day_of_the_month_label.grid(row=2, column=1,padx=10, pady=5, sticky=tk.W)
    thithi_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
    paksha_label.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)

    # Grid Row configuration
    root.grid_rowconfigure(0, weight=0, minsize=5)
    root.grid_rowconfigure(1, weight=3)
    root.grid_rowconfigure(2, weight=3)
    root.grid_rowconfigure(3, weight=3)

    # Grid Column configuration
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    # Element binding for events :
    # - Top layer (Main Label + Custom Header) events for mouse hover
    main_label.bind("<Enter>", lambda event: top_area_enter(event, button_frame))
    main_label.bind("<Leave>", lambda event: top_area_leave(event, button_frame))
    button_frame.bind("<Enter>", lambda event: top_area_enter(event, button_frame))
    button_frame.bind("<Leave>", lambda event: top_area_leave(event, button_frame))
    
    # - Custom drag and drop event
    button_frame.bind("<Button-1>", start_move_widget)
    button_frame.bind("<B1-Motion>", stop_move_widget)

    # Initialization of the main widget
    root.mainloop()

# Custom minimize functionality
def minimize_window(
        main_label, 
        maasa_label, 
        thithi_label, 
        paksha_label, 
        day_of_the_month_label, 
        maximize_button, 
        minimize_button
        ) :  
    maasa_label.grid_remove()
    thithi_label.grid_remove()
    paksha_label.grid_remove()
    day_of_the_month_label.grid_remove()
    main_label.grid_remove()
    maximize_button.pack(side=tk.RIGHT, padx=5)
    minimize_button.pack_forget()
    print("Called Mini")

# Custom maximize functionality when in minimized state
def maximize_window(
        main_label, 
        maasa_label, 
        thithi_label, 
        paksha_label, 
        day_of_the_month_label, 
        maximize_button, 
        minimize_button
        ) :
    main_label.grid(row=1, columnspan=2, padx=10, pady=8, sticky="nsew")
    maasa_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
    day_of_the_month_label.grid(row=2, column=1,padx=10, pady=5, sticky=tk.W)
    thithi_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
    paksha_label.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)
    minimize_button.pack(side=tk.RIGHT, padx=5)
    maximize_button.pack_forget()
    print("Called Maxi")

# Close the widget
def close_window() :
    root.destroy()

# Function to handle mouse enter event
def top_area_enter(event, button_frame) :
    button_frame.hover = False # Hover Flag to check if the mouse is still on the area
    button_frame.grid(row=0, column=0, columnspan=2,  sticky="ew", padx=0, pady=0) # Show the hidden custom header
    
    # Cancel any existing root.after job
    if hasattr(button_frame, 'after_id') :
        root.after_cancel(button_frame.after_id)

# Function to handle mouse leave event
def top_area_leave(event, button_frame) :
    button_frame.hover = True # Hide only if this flag is true
    
    # Cancel any existing root.after job
    if hasattr(button_frame, 'after_id') :
        root.after_cancel(button_frame.after_id)

    delay = 10000 # 10 seconds delay in milliseconds
    start_time = time.time() 

    # Schedule the delayed action directly
    button_frame.after_id = root.after(delay, lambda : check_and_remove_button_frame(button_frame))
    
    # Storing the start time in the frame for comparison later
    button_frame.start_time = start_time

# Function to remove the button frame if conditions are met
def check_and_remove_button_frame(button_frame) :
    if hasattr(button_frame, 'start_time') :
        
        # Check if the delay has actually passed
        if (time.time() - button_frame.start_time) > 10 : 
            remove_button_frame(button_frame)

# Function to remove the button frame
def remove_button_frame(button_frame) :
    if button_frame.hover :
        button_frame.grid_remove()

# Custom drag and drop functions
# Start
def start_move_widget(event) :
    root.x = event.x
    root.y = event.y

# Final position
def stop_move_widget(event) :
    x = event.x_root - root.x
    y = event.y_root - root.y
    root.geometry(f"+{x}+{y}")