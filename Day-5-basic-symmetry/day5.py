from PIL import Image
pic = Image.open('Cao.jpg')
[width, height] = pic.size
pixels = pic.load()

for x in range(width//2):
    for y in range(height):
        (r, g, b) = pixels[x, y]
        pixels[width-x-1, y]=(r, g, b)

pic.save('neg.jpg')
