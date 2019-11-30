"import requests 
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
		creat_dictionary(clean_up_list)
	
	def creat_dictionary(clean_word_list):
		word_count = {}
	"	for word in clean_word_list:
		if word in word_count:
			word_count[word] += 1
		else:
			word_count[word] += 1
	for key, value in sorted(word_count.items(), key =operator.itemgetter(1)):
		print(key, value)

start('')

