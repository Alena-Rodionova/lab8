import PIL
from PIL import Image

filename = "postcard.jpg"
with Image.open(filename) as img:
    img.load()

cropped_img = img.crop((100, 150, 800, 680))
# cropped_img.show()
cropped_img.save("cropped_postcard.jpg")