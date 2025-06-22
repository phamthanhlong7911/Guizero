class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    @property
    def balance(self):
        return self.balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self.balance = value
        else:
            raise ValueError("Dư không hợp lệ")

    def in_thong_tin(self):
        print(f"Số dư tài khoản là:{self.balance}")


hoc_sinh = BankAccount(1511)
hoc_sinh.in_thong_tin()
