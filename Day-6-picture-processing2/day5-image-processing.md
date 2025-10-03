# Image Processing

## 1. Blue filter on your picture
```python
from PIL import Image
import random

pic = Image.open('butterfly.jpg')

#get the size of the picture
[width, height] = pic.size
pixels = pic.load()

for x in range(width):
  for y in range(height):
    (r, g, b) = pixels[x, y]
    pixels[x, y] = (0, 0, b)

pic.save('newPic.jpg')
```

## 2. Salt and Pepper on your picture
```python
from PIL import Image
import random

pic = Image.open('butterfly.jpg')

#get the size of the picture
[width, height] = pic.size
pixels = pic.load()

for x in range(width):
  for y in range(height):
    (r, g, b) = pixels[x, y]
    noise = random.randint(-20, 20)
    pixels[x, y] = (r + noise, g+noise, b+noise)

pic.save('newPic.jpg')
```

## 3. Steganography Introduction

# bit.ly/day6-muirlands