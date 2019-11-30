import requests
from bs4 import beutifullsoup
import operator


def start(url):
	word_list = []
	source_code = requests.get(url).text
	for post_text in soup.findALL('a',{'class': 'index_singlelistTitle'}):
		content = post_text.string
		word = content.lower().split()
		for each_word in word:
			print(each_word)
			word_list.append(each_word)



start('https://mail.google.com/mail/u/0/#inbox/FMfcgxwGBwQNVSQczHzRXJMWtVzjfgrP')

