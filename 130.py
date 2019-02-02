import pytesseract
from PIL import Image
image = Image.open("D:/pic/pice.jpg")
result = pytesseract.image_to_string(image)
print(result)
