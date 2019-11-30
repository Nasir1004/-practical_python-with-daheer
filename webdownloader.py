from urllib import request
 
goog_url ='https://github.com/PROGRAMER678/python-with-tahir.git' 

def download_stock_data(cstv_url):
	response = request.urlopen(cstv_url)
	csv = response.read
	cstv_str = str(csv)
	lines = cstv_str.split("\\n")
	dest_url = r'goog.csv'
	fx =open(dest_url,"w")
	for lin in lines:
		fx.write(line + "\n")
	fx.close()

download_stock_data(goog_url)
