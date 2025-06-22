class Person:
    def __init__(self, name, age):
        self.__name = str(name)
        self._age = int(age)

    @property
    def age(self):
        return self._age

    def get_name(self):
        return self.__name

    @age.setter
    def age(self, value):
        if 100 >= value >= 10:
            self._age = value
        else:
            raise ValueError("Tuổi không hợp lệ")

    def in_thong_tin(self):
        print(f"Tên học sinh là:{self.__name}")
        print(f"Tuổi học sinh là:{self._age}")


hoc_sinh = Person(age=15, name="Phạm Thanh Long")
hoc_sinh.in_thong_tin()
