'''
from pil  import image

baby = image.open("baby.jpg")
black_white = baby.convert("l")


black_white.show("black.jpg")
 '''
from pil  import image
from pil  import imageFilter

sister = image.open('sister')
blur = sister.filter(imageFilter.BLUR)
detail = sister.filter (imageFilter.BLUR)
edges =  siter.filter(imageFilter.FIND_EDGES)

blur.show()
detail.show()
enges.show()

