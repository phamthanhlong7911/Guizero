from guizero import Text, App, Picture
app = App(title="chào mừng đến guizero", width=500, height=500, layout="auto", bg="light blue")
text = Text(app, "Hãy lập trình Gui cùng guizero", color="green", size= 18)
app.display()