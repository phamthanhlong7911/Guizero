class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return (f"tên của bạn là{self.name}, tuổi của bạn là{self.age}")


class Student(Person):
    def __init__(self, student_id, major, **kwargs):
        super().__init__(**kwargs)
        self.student_id = student_id
        self.major = major

    def introduce(self):
        return (f"""
{super().introduce()}
{self.student_id}
{self.major}
""")


class Teacher(Person):
    def __init__(self, teacher_id, subject, **kwargs):
        super().__init__(**kwargs)
        self.teacher_id = teacher_id
        self.subject = subject

    def introduce(self):
        return (f"""
{super().introduce()}
{self.teacher_id}
{self.subject}
""")


class TeachingAssistant(Student, Teacher):
    def __init__(self, name, age, student_id, major, teacher_id, subject):
        super().__init__(
            name=name,
            age=age,
            student_id=student_id,
            major=major,
            teacher_id=teacher_id,
            subject=subject)

    def introduce(self):
        return (f"""
{self.name}
{self.age}
{self.student_id}
{self.major}
{self.teacher_id}
{self.subject}
""")


c = TeachingAssistant("Nguyễn Phúc Khang", 14, 559595, "Văn", 284, "Anh")
print(c.introduce())
