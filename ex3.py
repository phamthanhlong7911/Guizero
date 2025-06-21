class Mat_hang():
    so_luong = int()

    def __init__(self, ten, so_luong, gia, ma_vach):
        self.ten = ten
        self._so_luong = so_luong
        self.__gia = gia
        self.__ma_vach = ma_vach

    def in_thong_tin(self):
        print(f"tên hàng:{self.ten}")
        print(f"số lượng hàng:{self._so_luong}")
        print(f"Giá bán  hàng:{self.__gia}")
        print(f"mã vạch của hàng:{self.__ma_vach}")

    def kiem_tra_kho(self, so_luong):
        if so_luong >= 100:
            print("Hàng nhiều")
        elif so_luong < 99 and so_luong >= 30:
            print("Hàng ổn định")
        elif so_luong < 30:
            print("Sắp hết hạn")

    def hien_so_luong(self):
        print(f"số lượng của hàng:{self.so_luong}")

    def lay_gia(self):
        return int(self.__gia)

    def cap_nhat_gia(self, gia_moi):
        if gia_moi <= 0:
            print("giá không hợp lệ")
        else:
            self.gia = gia_moi

    def lay_ma(self):
        return int(self.__ma_vach)

    def cap_nhap_ma(self, ma_moi):
        if len(ma_moi) >= 8 and len(ma_moi) <= 12:
            self.__ma_vach = ma_moi
        else:
            print("Mã không hợp lệ")

    def ban_so_luong(self, so_luong_ban):
        if so_luong_ban <= self._so_luong:
            self.so_luong -= so_luong_ban
            print("Bạn bán thành công")
        else:
            print("bạn không có đủ hàng để bán")


x = Mat_hang(ten="Bút", so_luong=200, gia=10000, ma_vach=50005531)
x.in_thong_tin()
x.hien_so_luong()
x.lay_gia()
x.cap_nhat_gia(150)
x.cap_nhap_ma(ma_moi="224242422")
x.__str__()
x.ban_so_luong(25)
x.kiem_tra_kho(100)
