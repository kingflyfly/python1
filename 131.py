import pytesseract
from PIL import Image
image = Image.open("D:/pic/{0}.jpg".format(3))
image = image.convert("L")
image.save('D:/pic/pice{0}.jpg'.format(3))


