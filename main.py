import requests
from bs4 import BeautifulSoup
import tkinter as tk

from infoRequest import get_panchang_html
from infoRequest import extract_panchang_block

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

def main():
    url = "https://www.drikpanchang.com/?geoname-id=1277333"
    html_content = get_panchang_html(url)
    if html_content :
        tag = 'div'
        maasa_class_name = 'dpPHeaderLeftTitle'
        thithi_class_name = 'dpPHeaderImage'
        maasa = extract_panchang_block(html_content, tag, class_name=maasa_class_name)
        thithi = extract_panchang_block(html_content, tag, class_name=thithi_class_name)
        if maasa :
            print("Got the Thithi !!")
            print(maasa)
            print(thithi)
        else :
            print("Sorry !")
    else :
        print("Failure !")
    

if __name__ == "__main__":
    panchang_window()
    main()