from guizero import TextBox, App, Box, PushButton, ListBox
import os

app = App(title="File Management", layout="grid")
dad = Box(app, layout="grid", grid=[1, 0])
txt = TextBox(dad, width=25, grid=[0, 0, 2, 1])


def load():
    list_file = os.listdir(folder_path)
    Tlist.clear()
    print(list_file)
    for file in list_file:
        Tlist.append(file)


def REMV():
    if not Tlist.value:
        app.warn("ERROR!", "Schedule is empty!")
    else:
        Tlist.remove(Tlist.value)


folder_path = "Test"


def crate():
    file_name = txt.value
    if file_name: 
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
    new_file = os.path.join(folder_path, file_name)
    exist_path = os.path.exists(new_file)
    files = os.listdir(folder_path)
    print(new_file)
    if not exist_path:
        print("hi")
        open(new_file, "w").close()
        Tlist.append(file_name)


def Ren():
    selected_file = Tlist.value
    new_name = txt.value
    if selected_file and new_name:
        file_path = os.path.join(folder_path, selected_file)
        print("file_path", file_path)
        new_path = os.path.join(folder_path, new_name)
        print("new_path", new_path)
        os.rename(file_path, new_path)
        load()


add = PushButton(dad, grid=[0, 1], text="crate", command=crate)
remv = PushButton(dad, grid=[1, 1], text="REMV", command=REMV)
Tlist = ListBox(app, width=200, height=100, grid=[0, 0])
remame = PushButton(dad, grid=[2, 1], text="Ren", command=Ren, args=[txt])
load()
app.display()
