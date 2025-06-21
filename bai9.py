# bai 9
from PIL import Image, ImageFilter
from guizero import *
app = App(title="Bai bao", width=500, height=500, layout="grid")
img1 = Image.open("cat1.png")
img2 = Image.open("hổ1.png")
img3 = Image.open("cat3.png")
img4 = Image.open("dog1.png")
new = (300, 200)
pic1 = img1.resize(new, Image.Resampling.LANCZOS)
pic2 = img2.resize(new, Image.Resampling.LANCZOS)
pic3 = img3.resize(new, Image.Resampling.LANCZOS)
pic4 = img4.resize(new, Image.Resampling.LANCZOS)

if pic1.mode == "RGBA" and pic2.mode == "RGBA" and pic3.mode == "RGBA" and pic4.mode == "RGBA":
    pic1 = pic1.convert("RGB")
    pic2 = pic2.convert("RGB")
    pic3 = pic3.convert("RGB")
    pic4 = pic4.convert("RGB")
flip1 = pic1.transpose(Image.FLIP_LEFT_RIGHT)
rotated_image = pic2.rotate(180, expand=True)
pict3 = pic3.crop((0, 0, 300, 150))
gaussian_blur = pic4.filter(ImageFilter.GaussianBlur(5))
picture1 = Picture(app, image=flip1, grid=[0, 0])
picture2 = Picture(app, image=rotated_image, grid=[1, 0])
picture3 = Picture(app, image=pict3, grid=[0, 1])
picture4 = Picture(app, image=gaussian_blur, grid=[1, 1])
app.display()