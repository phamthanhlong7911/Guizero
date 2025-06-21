from guizero import App, Text, TextBox, ListBox, PushButton


def them():
    a = textbox.value
    listbox.append(a)


def xoa():
    chon = listbox.value
    chon.clear()


app = App(title="công việc", layout="grid")
text = Text(app, text="DANH SÁCH CÁC VIỆC LÀM", grid=[1, 0])
text1 = Text(app, text="nhập công việc", grid=[0, 1])
textbox = TextBox(app, grid=[1, 1])
button = PushButton(app, text="Thêm", grid=[1, 2], command=them)
listbox = ListBox(app, grid=[0, 2], items=[])
button1 = PushButton(app, grid=[1, 3], text="Xóa", command=xoa)
app.display()
