import requests
from bs4 import BeautifulSoup

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
    main()