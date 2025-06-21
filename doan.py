from guizero import App, Text, PushButton, Box, Picture, TextBox, ListBox
kho = {}
danh_sach = []


def nhap_kho():
    trang_chinh.hide()
    nhap_kho_box.show()


def nhap_kho1():
    trang_chinh.hide()
    xem_kho_box.show()


def nhap_kho2():
    trang_chinh.hide()
    xuat_kho_box.show()


def quay_lai_nhap_kho():
    nhap_kho_box.hide()
    trang_chinh.show()


def quay_lai_xem_kho():
    xem_kho_box.hide()
    trang_chinh.show()


def quay_lai_xuat_kho():
    xuat_kho_box.hide()
    trang_chinh.show()


file_kho = "doan.txt"


def luu_vao_file():
    with open(file_kho, "w", encoding="utf-8") as f:
        for ten, data in kho.items():
            f.write(f"{ten},{data['gia']}, {data['so_luong']}\n")


def add1():
    ten = ten_hang_textbox_nhap_kho.value.strip().lower()
    print(ten)

    gia = float(gia_nhap_hang_textbox_nhap_kho.value)
    print(gia)
    so_luong = int(so_luong_nhap_kho.value)
    print(so_luong)
    if so_luong <= 10000:
        if ten in kho and gia == kho[ten]["gia"]:
            kho[ten]["so_luong"] += so_luong
            if kho[ten]["so_luong"] > 10000:
                app.info("info", "Số lượng vượt quá mức cho phép")
                return
            app.info("info", "Thành công")
        else:
            if ten in kho:
                app.info("info", "Tên đã tồn tại. Vui lòng nhập lại")
                return
            kho[ten] = {"so_luong": so_luong, "gia": gia}
            app.info("info", "Thành công")
    else:
        app.info("info", "Số lượng vượt quá mức cho phép")
    ten_hang_textbox_nhap_kho.clear()
    gia_nhap_hang_textbox_nhap_kho.clear()
    so_luong_nhap_kho.clear()
    luu_vao_file()


def show():
    listbox_xem_kho.clear()
    for ten, data in kho.items():
        listbox_xem_kho.append(f'{ten}-{data['gia']}đ-SL{data['so_luong']}')


def show1():
    listbox_xuat_kho.clear()
    for ten, data in kho.items():
        listbox_xuat_kho.append(f'{ten}-{data['gia']}đ-SL{data['so_luong']}')


def load():
    kho.clear()
    with open(file_kho, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(",")
            ten = parts[0]
            so_luong = int(parts[2])
            gia = float(parts[1])
            kho[ten] = {'so_luong': so_luong, 'gia': gia}
    print(kho)


def ban_hang():
    print(kho)
    s1 = int(so_luong_xuat_kho.value)
    chon = listbox_xuat_kho.value
    ten = chon.split("-")[0]

    if ten in kho and kho[ten]["so_luong"] > s1:
        kho[ten]["so_luong"] -= s1
        luu_vao_file()
        show1()
    if ten in kho and kho[ten]["so_luong"] == s1:
        kho[ten]["so_luong"] -= s1
        app.info("info", "ĐỒ Dùng này sắp hết hàng")

    if ten in kho and kho[ten]["so_luong"] < s1:
        app.info("info", "Số Lượng không đủ ")


def xoa_xem_kho():
    chon = listbox_xem_kho.value
    ten = chon.split("-")[0]
    build_a_snowman = app.yesno("A question...", "Bạn có muốn xóa không?")

    if build_a_snowman == True:
        del kho[ten]
        app.warn("Snowman", "Bạn đã xóa thành công!")
        show()

    else:
        app.info("Snowman", "Giữ lại")


app = App()
app.bg = "#A5FAC2"
trang_chinh = Box(app, layout="grid")
text = Text(trang_chinh, grid=[1, 0], text="TIỆM TẠP HÓA", size=30)
text.text_bold = True
text = Text(trang_chinh, grid=[1, 1], text="")
button1 = PushButton(trang_chinh, text="Nhập kho", grid=[0, 2], width=20, height=5, command=nhap_kho)
button1.bg = "#F07E6F"
button1.text_color = "White"
button1.text_bold = True
button2 = PushButton(trang_chinh, text="Kiểm kho", grid=[1, 2], width=20, height=5, command=nhap_kho1)
button2.bg = "#F07E6F"
button2.text_color = "White"
button2.text_bold = True
button3 = PushButton(trang_chinh, text="Xuất kho", grid=[2, 2], width=20, height=5, command=nhap_kho2)
button3.bg = "#F07E6F"
button3.text_color = "White"
button3.text_bold = True
# nhapkho
nhap_kho_box = Box(app, visible=False, layout="grid")
text_nhap_kho = Text(nhap_kho_box, text="Nhập Kho", size=35, grid=[2, 0])
text_nhap_kho.text_color = "Black"
text_nhap_kho.text_bold = True
emoji_nhap_kho = PushButton(nhap_kho_box, width=12, height=3, text="🔙", grid=[0, 0], command=quay_lai_nhap_kho)
ten_hang_nhap_kho = PushButton(nhap_kho_box, text="Tên hàng", grid=[1, 1], width=20, height=4)
ten_hang_nhap_kho.bg = "#222831"
ten_hang_nhap_kho.text_bold = True
ten_hang_nhap_kho.text_color = "White"
ten_hang_textbox_nhap_kho = TextBox(nhap_kho_box, grid=[2, 1], width=15, height=5, multiline=True, scrollbar=True)
gia_nhap_nhap_kho = PushButton(nhap_kho_box, text="Giá", grid=[1, 2], width=20, height=4)
gia_nhap_nhap_kho.bg = "#506F47"
gia_nhap_nhap_kho.text_bold = True
gia_nhap_nhap_kho.text_color = "White"
gia_nhap_hang_textbox_nhap_kho = TextBox(nhap_kho_box, grid=[2, 2], width=15, height=5, multiline=True, scrollbar=True)
text1 = Text(nhap_kho_box, text="", grid=[0, 0, 1, 3])
so_luong = PushButton(nhap_kho_box, grid=[1, 3], text="Số lượng", width=20, height=4)
so_luong.bg = "#6495ed"
so_luong.text_bold = True
so_luong.text_color = "#ffffff"
so_luong_nhap_kho = TextBox(nhap_kho_box, grid=[2, 3], width=15, height=5, multiline=True, scrollbar=True)
them_vao_kho_nhap_kho = PushButton(nhap_kho_box, text="Thêm vào kho", grid=[2, 5], width=20, height=4, command=add1)
them_vao_kho_nhap_kho.bg = "#F30000"
them_vao_kho_nhap_kho.text_bold = True
them_vao_kho_nhap_kho.text_color = "White"
# xemkho
xem_kho_box = Box(app, visible=False, layout="grid")
text_xem_kho = Text(xem_kho_box, text="Danh Sách Kho", size=35, grid=[1, 1])
text_xem_kho.text_color = "Black"
text_xem_kho.text_bold = True
emoji_xem_kho = PushButton(xem_kho_box, width=12, height=3, text="🔙", grid=[0, 0], command=quay_lai_xem_kho)
listbox_xem_kho = ListBox(xem_kho_box, items=[], grid=[1, 4, 2, 4], scrollbar=True, width=400, height=300)
lam_moi = PushButton(xem_kho_box, text="Làm Mới", grid=[1, 2], command=show, width=20, height=5)
lam_moi.bg = "#112a9b"
lam_moi.text_bold = True
lam_moi.text_color = "White"
xoa = PushButton(xem_kho_box, text="Xóa", grid=[1, 3], width=12, height=3, command=xoa_xem_kho)
xoa.bg = "#0033CC"
xoa.text_bold = True
xoa.text_color = "White"
# xuatkho
xuat_kho_box = Box(app, visible=False, layout="grid")
text_xuat_kho = Text(xuat_kho_box, text="Xuất Kho", size=35, grid=[2, 0])
text_xuat_kho.text_color = "Black"
text_nhap_kho.text_bold = True
emoji_xuat_kho = PushButton(xuat_kho_box, width=12, height=5, text="🔙", grid=[0, 0], command=quay_lai_xuat_kho)
so_luong = PushButton(xuat_kho_box, grid=[1, 3], text="Số lượng", width=15, height=5)
so_luong.bg = "#6495ed"
so_luong.text_bold = True
so_luong.text_color = "#ffffff"
so_luong_xuat_kho = TextBox(xuat_kho_box, grid=[4, 3], width=25, height=5, multiline=True, scrollbar=True)
listbox_xuat_kho = ListBox(xuat_kho_box, items=[], grid=[1, 6, 4, 4], scrollbar=True, width=400, height=300)
lam_moi_xuat = PushButton(xuat_kho_box, text="Làm Mới", grid=[2, 5], command=show1, width=20, height=5)
lam_moi_xuat.text_bold = True
lam_moi_xuat.text_color = "#ffffff"
ban = PushButton(xuat_kho_box, grid=[2, 4], text="bán", width=15, height=5, command=ban_hang)
ban.bg = "#ac1a2d"
ban.text_bold = True
ban.text_color = "White"
lam_moi_xuat.bg = "#92bb3f"
load()
app.display()
