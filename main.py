from bs4 import BeautifulSoup
import tkinter as tk

# Custom function import
from infoRequest import get_panchang_html
from infoRequest import extract_panchang_block
from panchangWidget import panchang_window
from extractor import info_extract

def main():
    # My source of information
    url = "https://www.drikpanchang.com/?geoname-id=1277333"
    html_content = get_panchang_html(url)
    
    # Extract the required information
    if html_content :
        tag = 'div'
        maasa_class_name = 'dpPHeaderLeftTitle'
        thithi_class_name = 'dpPHeaderImage'
        maasa = extract_panchang_block(html_content, tag, class_name=maasa_class_name)
        thithi = extract_panchang_block(html_content, tag, class_name=thithi_class_name)
        if maasa :
            print("Got the Thithi !!")
            panchang_object = info_extract(maasa, thithi)
        else :
            print("Sorry !")
    else :
        print("Failure !")
    panchang_window(panchang_object)

if __name__ == "__main__":
    main()