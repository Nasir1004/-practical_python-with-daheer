import requests
from bs4 import Beautifulsoup


def trade_spider(max_pages):
    page = 1
    while page <=max_pages:
        url = "https://ww25.buckysroom.org/trade/view.php?page=" + str(page)
        source_code = requests.get(url)
        plain.text =source_code.text
        soup =Beautifulsoup(plain_text)
        for link in soup.findALL('a',{'class':'item name'}):
            href = "https://buckysroom.og" + link.get('href')
            title = link. string
            print(href)
            print(title)
        page += 1


def get_single_item_data(item_url):
    source_code = requests.get(url)
    plain.text =source_code.text
    soup =Beautifulsoup(plain_text)
    for item_name in soup.findALL('div',{'class': 'i-name'}):
        print(item_name.string)
    for link in soup.findALL('a'):
        href ='https://buckysroom.org' + link.get('href')
        print(href)



trade_spider(3)



