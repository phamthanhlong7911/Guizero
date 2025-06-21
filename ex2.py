class Car:
    mileage = 10
    engine_on = False
    battery_level = 100
    fuel_level = 50

    def __init__(self, color, brand, year, mileage, engine_on, car_type, battery_level, fuel_level):
       self.color = color
       self.brand = brand
       self.year = year
       self.mileage = mileage
       self.engine_on = engine_on
       self.car_type = car_type
       self.battery_level = battery_level
       self.fuel_level = fuel_level

    def started_engine(self):
        self.engine_on = True
        print(f"Xe {self.brand} khởi động")

    def stopped_engine(self):
        self.engine_on = False
        print(f"Xe {self.brand} tắt máy")

    def drive(self, car_type):
        self.car_type == "electronic" or self.car_type == "gasoline"
        if self.car_type == "electronic":
            self.battery_level = 100
            self.battery_level = self.battery_level - self.mileage
            if self.battery_level < 10:
                print("ko thể chạy")
        if self.car_type == "gasoline":
            self.fuel_level = 20
            self.fuel_level = self.fuel_level - (self.mileage / 15)
            if self.fuel_level < 5:
                print("ko thể chạy")

    def charge(self):
        if self.car_type == "electronic":
            self.battery_level = 100
            print("Xe đã được sạc đầy")
        else:
            print("Xe xăng không thể sạc")

    def refuel(self, amount):
        if self.car_type == "Xăng":
            self.fuel_level += amount
            print(f"Đã đổ thêm {amount} lít xăng. Tổng xăng: {self.fuel_level}")
        else:
            print("Xe điện không đổ xăng")

    def paint(self, new_color):
        self.color = new_color
        print(f"Xe đã được sơn lại màu {new_color}")

    def in_thong_tin(self):
        print(f"Màu xe:{self.color}")
        print(f"Hãng xe:{self.brand}")
        print(f"Năm sản xuất:{self.year}")
        print(f"Số cây đã đi:{self.mileage}")
        print(f"Tình trạng động cơ:{self.engine_on}")
        print(f"Loại xe:{self.car_type}")
        print(f"Số pin còn lại:{self.battery_level}")
        print(f"Số xăng còn lại:{self.fuel_level}")



x = Car(brand="Tesla", color="White", year=2022, car_type="electronic", mileage=0, engine_on=True, battery_level=20, fuel_level=0)
x.in_thong_tin()
x.started_engine()
x.drive(50)
x.stopped_engine()
x.drive(10)
x.charge()
x.in_thong_tin()
y = Car(brand="Toyota", color="Black", year=2020, car_type="gasoloine", mileage=0, engine_on=False, battery_level=0, fuel_level=30)
y.started_engine()
y.drive(120)
y.stopped_engine()
y.drive(40)
y.refuel(20)
y.in_thong_tin()
