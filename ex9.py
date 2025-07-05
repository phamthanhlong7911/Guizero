from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def dien_tich():
        pass

    def chu_vi():
        pass


class Circle(Shape):
    def __init__(self, ban_kinh):
        self.ban_kinh = ban_kinh

    def dien_tich(self):
        return int(self.ban_kinh) ^ 2 * 3.14
