from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def started_engine(self):
        pass

    @abstractmethod
    def stopped_engine(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Car(Vehicle):
    def started_engine(self):
        self.started_engine = True
        print("Xe hơi đã khởi động")

    def stopped_engine(self):
        self.stopped_engine = False
        print("Xe hơi đã tắt máy")

    def move(self):
        if not self.started_engine == True:
            print("Hãy khởi dộng xe")
        else:
            print("Xe có thể chạy")


class Bike(Vehicle):
    def move(self):
        print("Xe đã chạy")


class Boat(Vehicle):
    def started_engine(self):
        self.started_engine = True
        print("tàu đã khởi động")

    def stopped_engine(self):
        self.stopped_engine = False
        print("tàu đã tắt máy")

    def move(self):
        if not self.started_engine == True:
            print("Hãy khởi dộng tàu")
        else:
            print("tàu có thể chạy")


x = Car()
x.started_engine()
