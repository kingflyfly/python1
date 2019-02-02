import pytesseract
from PIL import Image
image = Image.open("D:/pic/7.jpg")
image = image.convert("L")
threshold = 170
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image = image.point(table,"1")
print(table)
image.save('D:/pic/pice.jpg')