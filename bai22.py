from guizero import App, Text, TextBox, PushButton, ListBox
import os

with open("fhrfr.txt", "w", encoding="utf-8") as f:
    f.write("Long quá đẹp trai")


def show_meme1(a):
    with open(a, "r", encoding="utf-8") as f:
        text_box.value = f.read()


# def update():
#     with open("fhrfr.txt", "w", encoding="utf-8") as f:
#         f.write(text_box.value)


def listfile():
    list_f = []
    for i in os.listdir():
        if i.endswith("txt"):
            list_f.append(i)
    return list_f


def choose_file():
    show_meme1(list_box.value)


app = App(layout="grid")
text = Text(app, text="", grid=[0, 0])
text_box = TextBox(app, width=50, text="", height=20, scrollbar=True, multiline=True, grid=[1, 0])
button = PushButton(app, text="Update", grid=[2, 0])
list_box = ListBox(app, grid=[3, 0], items=listfile(), command=choose_file)
# show_meme1()
app.display()
