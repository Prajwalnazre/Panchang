import requests
from bs4 import BeautifulSoup
import tkinter as tk

root = tk.Tk()

def get_html(url) :
    response = requests.get(url)
    if response.status_code == 200 :
        return response.text
    else :
        return None
    
def extract_block(html, tag, class_name) :
    soup = BeautifulSoup(html, 'html.parser')
    if class_name:
        block = soup.find(tag, class_=class_name)
    else :
        block = soup.find(tag)
    for child in block.children : 
        if child.name == 'img' :
            return child
        else :
            return block.string

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
    html_content = get_html(url)
    if html_content :
        tag = 'div'
        maasa_class_name = 'dpPHeaderLeftTitle'
        thithi_class_name = 'dpPHeaderImage'
        maasa = extract_block(html_content, tag, class_name=maasa_class_name)
        thithi = extract_block(html_content, tag, class_name=thithi_class_name)
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