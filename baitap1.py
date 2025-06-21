from guizero import App, Text, TextBox, Box, PushButton


def ham():
    a = float(toan.value)
    b = float(van.value)
    c = float(anh.value)
    d = (a+b+c)/3
    lam_tron = round(d, 2)  # Làm tròn đến 2 chữ số thập phân
    print(lam_tron)
    cau = Text(box, grid=[1, 8])

    if d < 5:
        cau.value = {f"điêm trung binh là:{lam_tron}-học lực yếu"}
    if d >= 5 and d < 7:
        cau.value = {f"điêm trung binh là:{lam_tron}-học lực trung bình"}
    if d > 7:
        cau.value = {f"điêm trung binh là:{lam_tron}-học lực tốt"}

app = App()
box = Box(app, layout="grid")
text1 = Text(box, text="Nhập điểm của bạn", grid=[1, 0])
text1.text_color = "Blue"
text1.size = 30
text2 = Text(box, text="Điểm toán:", grid=[1, 1])
toan = TextBox(box, grid=[1, 2])
text3 = Text(box, text="Điểm văn:", grid=[1, 3])
van = TextBox(box, grid=[1, 4])
text4 = Text(box, text="Điểm anh:", grid=[1, 5])
anh = TextBox(box, grid=[1, 6])
diem_trung_binh = PushButton(box, grid=[1, 7], width=15, height=4, command=ham)
app.display()
