class Item:
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author


class Book(Item):
    def __init__(self, id, title, author, page):
        super().__init__(id, title, author)
        self.page = page

    def printInfo(self):
        print(self.id)
        print(self.title)
        print(self.author)
        print(self.page)


class DVD(Item):
    def __init__(self, id, title, author, duration):
        super().__init__(id, title, author)
        self.duration = duration

    def printInfo(self):
        print(self.id)
        print(self.title)
        print(self.author)
        print(self.duration)


class Magazine(Item):
    def __init__(self, id, title, author, issue):
        super().__init__(id, title, author)
        self.issue = issue

    def printInfo(self):
        print(self.id)
        print(self.title)
        print(self.author)
        print(self.issue)


danh_sach = [
    Book("B001", "Python Programming", "Nguyen Van A", 320),
    DVD("D001", "Learning Python", "Tran Thi B", 90),
    Magazine("M001", "Tech Monthly", "Le Van C", "2025-06"),
    ]
for item in danh_sach:
    item.printInfo()
