from guizero import Drawing, App, Combo, Text


def choice_answer(a):
    a = combo.value
    if a == "Long":
        text.value = "buồn"
    else:
        text.value = "Yêu đời"


app = App()
text1 = Text(app, )
drawing = Drawing(app)
# drawing.rectangle(0, 50, 100, 100, color="Blue", outline=True, outline_color="Black")
# drawing.triangle(400, 350, 410, 550, 440, 100, color="red")
text = Text(app)
combo = Combo(app, options=["", "Long", "Thái", "Hùng"], command=choice_answer)
app.display()
