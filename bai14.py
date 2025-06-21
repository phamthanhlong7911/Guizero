from guizero import App, PushButton, Text, Box
import random
app = App(title="Đi tìm gián điệp",  width=500, height=500)
text = Text(app, text="Đi tìm gián điệp")
box = Box(app, layout="grid")
button1 = PushButton(box, text="?", grid=[0, 0], width=10, height=5)
button2 = PushButton(box, text="?", grid=[1, 0], width=10, height=5)
button3 = PushButton(box, text="?", grid=[2, 0], width=10, height=5)
button4 = PushButton(box, text="?", grid=[0, 1], width=10, height=5)
button5 = PushButton(box, text="?", grid=[1, 1], width=10, height=5)
button6 = PushButton(box, text="?", grid=[2, 1], width=10, height=5)
button7 = PushButton(box, text="?", grid=[0, 2], width=10, height=5)
button8 = PushButton(box, text="?", grid=[1, 2], width=10, height=5)
button9 = PushButton(box, text="?", grid=[2, 2], width=10, height=5)
x = random.randint(0, 8)

app.display()