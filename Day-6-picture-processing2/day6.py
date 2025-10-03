from PIL import Image
import random

pic = Image.open('cao.jpg')
[width, height] = pic.size
pixels = pic.load()

for x in range(width):
    for y in range(height):
        (r, g, b) = pixels[x, y]
        noise = random.randint(-20, 20)
        pixels[x, y] = (r+noise, g+noise, b+noise)

pic.save('result.jpg')