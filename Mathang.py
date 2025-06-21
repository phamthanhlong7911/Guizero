from ex3 import Mat_hang
from guizero import App, Text, ListBox, TextBox, PushButton

danh_sach_mat_hang = [
    Mat_hang("gà", 100, 1000000, 12345678),
    Mat_hang("bò", 120, 1200000, 12345678),
    Mat_hang("sữa", 80, 50000, 12345678)
]

ten_mat_hang = [mh.ten for mh in danh_sach_mat_hang]


def TimHang(ten):
    mh = input
    for mh in danh_sach_mat_hang:
        if danh_sach_mat_hang.ten == ten:
            print(mh)


def HienThongtin():
    ten_duoc_chon = o_hien_thong_tin.value
    for mh in danh_sach_mat_hang:
        if mh.ten == ten_duoc_chon:
            text1.value = f"Tên: {mh.ten}"
            text2.value = f"Số lượng: {mh._so_luong}"
            text3.value = f"Giá: {mh.lay_gia()}" 
            text4.value = f"Trạng thái kho: {mh.kiem_tra_kho()}"
            text5.value = f"Mã vạch của sản phẩm: {mh.__ma_vach}"
            break


def BanHang():
    hang_duoc_ban = o_hien_thong_tin.value
    for hb in danh_sach_mat_hang:
        if hb.ten == hang_duoc_ban:
            hb.ban_so_luong(int(textboxban.value))
            HienThongtin()
            break


def CapNhatGia():
    ten = o_hien_thong_tin.value
    for mh in danh_sach_mat_hang:
        if mh.ten == ten:
            mh.cap_nhat_gia(int(o_nhap_gia_moi.value))
            HienThongtin()
            break


def Cap_Nhat_Ma_Vach():
    ten = o_hien_thong_tin.value
    for mh in danh_sach_mat_hang:
        if mh.ten == ten:
            mh.cap_nhap_ma(str(o_nhap_ma_vach.value))
            HienThongtin()
            break


app = App(title="siêu thị")
o_hien_thong_tin = ListBox(app, items=ten_mat_hang, command=HienThongtin)
text1 = Text(app)
text2 = Text(app)
text3 = Text(app)
text4 = Text(app)
text5 = Text(app)
o_nhap_gia_moi = TextBox(app)
nut_bam1 = PushButton(app, text="Cập nhật giá", command=CapNhatGia)
textboxban = TextBox(app)
nut_bam = PushButton(app, text="Bán hàng", command=BanHang)
o_nhap_ma_vach = TextBox(app)
nut_bam2 = PushButton(app, text="Cập nhật mã vạch", command=Cap_Nhat_Ma_Vach)
app.display()
