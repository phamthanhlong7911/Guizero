from guizero import *
app = App(title="idk", width=1000, height=1000, layout="grid", bg=(137, 207, 240))
box_book = Box(app, grid=[0,0])
picture = Picture(box_book, image="cat1.png", width=200, height=150)

box_book2 = Box(app,  grid=[1,0])
picture = Picture(box_book2, image="cat3.png", width=200, height=150)

box_book3 = Box(app,  grid=[2, 0, 1, 2])
picture = Picture(box_book3, image="cat2.png", width=200, height=300)

box_book4 = Box(app,  grid=[0, 1, 2, 1])
picture = Picture(box_book4, image="voi1.png", width=400, height=150)

box_book5 = Box(app,  grid=[0, 2, 2, 1])
picture = Picture(box_book5, image="khỉ1.png", width=400, height=150)

box_book6 = Box(app,  grid=[2, 2])
picture = Picture(box_book6, image="hổ1.png", width=200, height=150)

app.display()