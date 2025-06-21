from PIL import Image
image = Image.open("cat1.png")

new_size = (500, 1000)
resized_img = image.resize(new_size, Image.Resampling.LANCZOS)
if image.mode == "RGBA":
    image = image.convert("RGB")
x = resized_img.crop((300, 500, 400, 700))
y = x.rotate(100, expand=True)
# z = y.transpose(Image.FLIP_LEFT_RIGHT)
y.show()
