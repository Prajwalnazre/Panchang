'''
Functions :
>> get_panchang_html(url)
- HTML Response of the complete page
- Used in main.py
>> extract_panchang_block(html, tag, class_name)
- Function to parse the HTML and get the required contents
- Used in main.py
'''

from bs4 import BeautifulSoup
import requests

# HTML Response of the complete page
def get_panchang_html(url) :
    response = requests.get(url)
    if response.status_code == 200 :
        return response.text
    else :
        return None

# Function to parse the HTML and get the required contents
def extract_panchang_block(html, tag, class_name) :
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