from guizero import App, PushButton, Text


def button_pressed():
    name = app.question("Hello", "What's your name ")
    if name is not None:
        hello.value = "Hello" + name


app = App()
hello = Text(app)
button = PushButton(app, command=button_pressed, text="Hello")
app.display()