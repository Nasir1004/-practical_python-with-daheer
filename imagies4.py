from pil import image

sister = image.open("sister.jpg")
nasir = image.open("nasir.jpg")
r1, g1, b1 = sister.split()
r2, g2, b2 = nasir.split()


new_img = image.merge("RGB", (r2, g1, b2))
new_img.show()
