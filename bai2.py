from guizero import Text, App, Picture
app = App(title="Hộp quà ma thuật", width=500, height=500, layout="auto", bg=(137,207,240))
text1 = Text(app, "Chào mừng đén với hộp quà ma thuật")
picture = Picture(app, "screenshot_1736682062.png", width=300, height=300)
text2 = Text(app, "Khám phá những điều kỳ diệu bên trong", color="green", size=10)
app.display()