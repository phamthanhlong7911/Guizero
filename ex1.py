class SinhVien:
    def __init__(self, ho_ten, ma_sv, lop, diem_tb):
        self.ho_ten = ho_ten
        self.ma_sv = ma_sv
        self.lop = lop
        self.diem_tb = diem_tb
    def in_thong_tin(self):
        print(f"Họ tên sinh viên:{self.ho_ten}")
        print(f"Mã sinh viên:{self.ma_sv}")
        print(f"Lớp của sinh viên:{self.lop}")
        xep_loai = ""
        if self.diem_tb >= 8:
            xep_loai = "Giỏi"
        elif self.diem_tb >= 6.5 and self.diem_tb < 8:
            xep_loai = "Khá"
        elif self.diem_tb >= 5 and self.diem_tb < 6.5:
            xep_loai = "Trung Bình"
        elif self.diem_tb <0:
            xep_loai = "Yếu"
        print(f"xếp loại:{xep_loai}")
        if self.diem_tb>10 or self.diem_tb<0:
            print("điểm k hợp lệ")

x = SinhVien(ho_ten="Phạm Thanh Long", ma_sv=20, lop=8, diem_tb=9.3)
x.in_thong_tin()
x.lop = 9
x.in_thong_tin()
y = SinhVien(ho_ten="Phạm Thanh Long", ma_sv=22, lop=9, diem_tb=9.5)
z = SinhVien(ho_ten="Cristiano Ronaldo", ma_sv=7, lop=11, diem_tb=7)
t = SinhVien(ho_ten="Trang", ma_sv=38, lop=5, diem_tb=11)
y.in_thong_tin()
z.in_thong_tin()
t.in_thong_tin()
