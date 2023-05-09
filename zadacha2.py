from PIL import Image
d = {1: "postcard.jpg", 2: "8marta.jpg", 3: "Dlove.jpg", 4: "dr.jpg"}

print("1 - Встреча с другом\n"
      "2 - 8 марта\n"
      "3 - День влюбленных\n"
      "4 - День рождения")
ans = int(input("Для получения открытки введите номер прадника : "))

filename = d[ans]
with Image.open(filename) as img:
    img.load()

img.show()
print("Хорошего праздника!")