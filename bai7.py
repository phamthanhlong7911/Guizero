from PIL import Image
image = Image.open("cat1.png")
if image.mode == "RGBA":
    image = image.convert("RGB")
# image.thumbnail((2000,1000))
new_size = (200, 300)
resized_img = image.resize(new_size, Image.Resampling.LANCZOS)
resized_img.show()