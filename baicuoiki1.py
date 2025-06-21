from guizero import App, Text, PushButton, Drawing
from random import randint
from PIL import Image


def quay():
    numbers = [str(randint(0, 9)) for i in range(6)]
    text1.value = "".join(numbers)


app = App(title="Xổ số đơn giản", width=600, height=400)
drawing = Drawing(app, width="fill", height="fill")
drawing.image(0, 0, "screenshot_1736682062.png", width=800, height=400)  
text = Text(app, text="Con số may mắn", size=20, color="blue", font="Arial")
text.size = 70
text1 = Text(app, text=" ", size=24, color="red", font="Courier")
text1.size = 70
button = PushButton(app, text="Quay số", command=quay)
app.display()
