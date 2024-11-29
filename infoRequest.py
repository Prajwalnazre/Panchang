from bs4 import BeautifulSoup
import requests

def get_panchang_html(url) :
    response = requests.get(url)
    if response.status_code == 200 :
        return response.text
    else :
        return None

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
