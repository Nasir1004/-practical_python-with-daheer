import requests
from bs4 import Beutifullsoup


def trade_spider(max_pages):
	page = 1
	while page < max_pages:
		url = ''
		source_code = requests.get(url)
		plain_text =