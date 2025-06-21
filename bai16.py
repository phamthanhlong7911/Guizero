from guizero import App, Text, TextBox, Box, PushButton, ListBox, info


def ham():
    Task = textbox.value
    if Task:
        list.append(Task)
        save_task()
    else:
        info(title="Canh Bao", text="Ban khong nhap cong viec")


def xoa():
    list.remove(list.value)


def save_task():
    with open("tes.txt", "w", encoding="utf-8") as f:
        for i in list.items:
            f.write(f"{i}\n")
    with open("tes.txt", "r", encoding="utf-8") as f:
        f.read()


def load_task():
    with open("tes.txt", "r", encoding="utf-8") as f:
        for i in f:
            list.append(i)


app = App()
box = Box(app, layout="grid")
text = Text(box, text="cong viec", grid=[0, 0])
textbox = TextBox(box, grid=[1, 0], width=50, height=50)
push1 = PushButton(box, text="Them", grid=[2, 0], command=ham)
push1.text_color = "Blue"
push2 = PushButton(box, text="xoa", grid=[2, 1], command=xoa)
push2.text_color = "red"
list = ListBox(app, height="fill",  width="fill")
list.bg = "LightYellow"
load_task()
app.display()
