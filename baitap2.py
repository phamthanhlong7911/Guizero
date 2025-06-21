from guizero import App, Text, PushButton, TextBox
import random


def random_a():
    b = textbox.value
    number = random.randint(0, 100)
    print(number)

    if number == b:
        app.info("info", "Bạn đoán đúng rồi")
    else:
        app.info("info", "Bạn đoán sai rồi")


app = App(title="Random number")
text = Text(app, text="Đoán 1 số từ 1 đến 100")
textbox = TextBox(app)
button = PushButton(app, text="Kiểm Tra", command=random_a)
app.display()
