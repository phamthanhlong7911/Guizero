from guizero import App, Text, TextBox, ButtonGroup, PushButton, Slider, Box, Combo, Drawing, ListBox


def add_meme():
    drawing.clear()
    x_position = slider_x.value
    y_position = slider_y.value
    drawing.image(0, 0, image=f"icon\{combo_meme.value}.png", width=400, height=400)
    drawing.text(x_position, y_position, text=boxtext.value, font=Button_Group.value, color=combo.value)


app = App()
app.bg = "#FFCC66"
box = Box(app, layout="grid")
box.bg = "#B0C4DE"
text1 = Text(box, text="Enter text", grid=[0, 0])
text1.text_color = "#FF0000"
boxtext = TextBox(box, grid=[1, 0])
text_button = PushButton(box, grid=[2, 0], text="ADD")
text2 = Text(box, text="select text color", grid=[0, 1])
text2.text_color = "#8A2BE2"
combo = Combo(box, options=["Black", "White", "Red", "Green", "Blue", "Brown", "Orange"], grid=[1, 1])
text3 = Text(box, text="select text font", grid=[0, 2])
text3.text_color = "#0000EE"
Button_Group = ButtonGroup(box, options=["Arial", "Times New Roman", "Calibri"], grid=[1, 2], selected="Times New Roman")
Button_Group.bg = "#00EEEE"
box1 = Box(app, layout="grid")
Text_meme = Text(box1, text="Select", grid=[0, 0])
combo_meme = Combo(box1, grid=[2, 0], options=["anh1", "anh2", "anh3"])
text_x = Text(box1, text="X", grid=[0, 1], color="Black", size=24)
slider_x = Slider(box1, grid=[1, 1], start=0, end=400)
text_y = Text(box1, text="Y", grid=[0, 2], color="Black", size=24)
slider_y = Slider(box1, grid=[1, 2], start=0, end=400)
drawing = Drawing(app, height=400, width=400)
drawing.bg = "White"
text_button = PushButton(box, grid=[2, 0], text="ADD", command=add_meme)
app.display()
