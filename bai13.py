from guizero import App, PushButton, Text
import random
# app = App(title="bài random", height=500, width=500)


def random_a():
    number = random.randint(0, 100)
    text.value = number


app = App(title="Random number")
text = Text(app)
text2 = Text(app, text="Hi")
button = PushButton(app, text="Tạo số", command=random_a)
app.display()