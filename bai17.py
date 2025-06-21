from guizero import App, Text, TextBox, Box, PushButton, ListBox, info


def ham():
    list.append(textbox.value)





app = App()
box = Box(app, layout="grid")
text = Text(box, text="cong viec", grid=[0, 0])
textbox = TextBox(box, grid=[1, 0], width=50, height=50)
push1 = PushButton(box, text="Them", grid=[2, 0], command=ham)
push1.text_color = "Blue"
push1 = PushButton(box, text="xoa", grid=[2, 0], command=ham)
push1.text_color = "Red"
list = ListBox(app, height="fill", width="fill")
list.bg = "Yellow"
app.display()