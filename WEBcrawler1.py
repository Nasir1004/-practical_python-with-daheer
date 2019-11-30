import requests 
	from bs4 import beautifullsoup
	import operator
	
	
	def start(url):
		word_list=[]
		source_code = request.get(url).text
		soup = beautifullsoup(source_code)
		for post_text in soup.findALL('a', {'class': ''})
		content = post_text.string
		word =content.lower().split()
		for each_word in words:
	
	clean_up_list(word_list)
	
	def clean_up_list(word_list):
		clean_word_list =[]
		for word in word_list:
			symbols = ""
			for i in range(0, len(symbols[i])):
				word = word.replace(symbols[i], "")
			if  len(word) > 0:
				clean_up_list.append(word)
	