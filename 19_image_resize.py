# Project 19
# Image Resizer

# pip install pillow

from PIL import Image

image = Image.open('test.jpg')
print("Current Size:", image.size)

resized_image = image.resize((500,500))
resized_image.save('test2.jpg')
