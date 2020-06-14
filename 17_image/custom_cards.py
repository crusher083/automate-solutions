from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os

with open('guests.txt', 'r') as f:
    guests = [line.rstrip() for line in f]
os.makedirs('cards', exist_ok=True)
flower = Image.open('flower.png')
for name in guests:
    border = Image.new('RGBA', (1300, 1020), 'black')
    inv = Image.new('RGBA', (1260, 980), 'white')
    W, H = border.size
    border.paste(inv, (20, 20))
    draw = ImageDraw.Draw(border)
    w, h = draw.textsize(name)
    font = ImageFont.truetype('HARLOWSI.TTF', 100)
    draw.text(((W-w)/2, 300), name, fill='black', font=font)
    border.paste(flower, (40, 500), flower)
    inv_name = f'{name}_card.png'
    border.save(os.path.join('cards', inv_name))


