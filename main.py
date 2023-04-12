from PIL import Image, ImageDraw, ImageFont
font = ImageFont.truetype('CodeNext-Trial-Regular.ttf', size=200)

img='crop.jpg'
with Image.open(img) as img:
    img.load()
img=img.crop((0, 380, img.width, img.height))
img.save('cropped.jpg')

hol={'Новый год': 'ny.jpg', 'Рождество': 'chr.jpg', 'Пасха': 'east.jpeg', '8 марта': 'women.jpg', 'День труда': 'fm.jpg'}
ans=input('Какой праздник?')
name=input('Какое имя?')
for key in hol:
    if ans==key:
        im=hol[key]
        im=Image.open(hol[key])
        font = ImageFont.truetype('CodeNext-Trial-Regular.ttf', size=im.width // 20)
        # im.show()
        img = ImageDraw.Draw(im)
        img.text(
            (im.width//5, 10),
            name + ', поздравляю',
            font=font,
            fill='#FF0000',
            stroke_width=2,
            stroke_fill="#FF0000")
        im.show()
else:
    print('Нет такой открытки(')



