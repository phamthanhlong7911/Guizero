from guizero import App, PushButton, Text
score = 0


def Score1():
    global score
    score += 1
    text.value = f"score{score}"
    app.bg = "red"
    app.text_color = "black"


def Score2():
    global score
    score += 1
    text.value = f"score{score}"
    app.bg = "blue"
    app.text_color = "black"


def Score3():
    global score
    score += 1
    text.value = f"score{score}"
    app.bg = "green "
    app.text_color = "black"


app = App(width=500, height=500, layout="grid")
text = Text(app, text="Score1.0", grid = [0,0])
button1 = PushButton(app, text = " màu đỏ", command=Score1, grid=[1, 0])
button2 = PushButton(app, text = " màu xanh", command=Score2, grid=[2, 0])
button3 = PushButton(app, text = " màu lá", command=Score3, grid=[3, 0])
app.display()
