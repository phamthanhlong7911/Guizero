class Student():
    def __init__(self, ten, diem, position):
        self.ten = ten
        self.diem = diem
        self.position = position
    def leader(self):
        print(f" tên sinh viên:{self.ten}")
        print(f"điểm :{self.diem}")
        print(f"chức vụ của mỗi sinh viên:{self.position}")

x = Student("Long", "10", "President")
x.leader()