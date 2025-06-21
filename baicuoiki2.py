from guizero import App, Box, ListBox, PushButton, TextBox, Combo, Slider
import os


def change_text_color():
    textbox.text_color = color_combo.value


def change_font():
    textbox.font = font_combo.value


def change_font_size():
    textbox.text_size = font_size_slider.value


app = App("Quản lý Tệp Văn Bản", width=600, height=400)
box = Box(app, width="fill", height="fill")
listbox = ListBox(box, width=20, height=10)
load_files_button = PushButton(box, text="Tải Tệp")
textbox = TextBox(box, width=40, height=10)
save_button = PushButton(box, text="Lưu")
color_combo = Combo(box, options=["Black", "Red", "Green", "Blue", "Purple"], command=change_text_color)
color_combo.value = "Black"  # Mặc định là màu đen
font_combo = Combo(box, options=["Arial", "Courier", "Times"], command=change_font)
font_combo.value = "Arial"  # Mặc định là Arial
font_size_slider = Slider(box, width=20, command=change_font)
font_size_slider.value = 12
app.display()


