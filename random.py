import random
import urllib,request


def download_web_image(url):
	name = random.randrange(1, 1000)
	full_name = str(name) + ".jpg"
	urllib.request.urllib(url, full_name)

download_web_image("https://www.facebook.com/photo.php?fbid=2475304369347857&set=a.1376069612604677&type=3&theater")
