from PIL import Image, ImageDraw, ImageFont


name = input("Введите имя получателя: ")
filename = "postcard.jpg"
with Image.open(filename) as img:
    img.load()
# используется файл с жирными символами шрифта Arial
font = ImageFont.truetype("BOOZY BOLD OUTLINE.ttf", 70)
draw_text = ImageDraw.Draw(img)
draw_text.text(
    (img.width // 2 - 100, 90),
    name + ", поздравляю!",
    font=font,
    fill=('#FF0000')
)
img.show()
img.save(name + "_postcard.png")