from  pil import  image

sister = image.open('screenshot(1).jpg')
girl = image.open("girl.png")

area = (100,100,300,300)
sister.paste(girl,area)

sister.show()
