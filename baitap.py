from guizero import App, Text, PushButton, Box, info
from random import choice
app = App(title="Chọn câu trả lời đúng",  width=500, height=500)
text1 = Text(app, text="Trắc nghiệm python", size=30, font="Times New Roman")
text2 = Text(app, text="ngôn ngữ dùng để phát triển web")
box = Box(app, layout="grid")

list = [
    {"question": "Ngôn ngữ nào dùng để phát triển web?", "options": ["Python", "HTML", "C++", "Java"], "answer": "HTML"},
    {"question": "Câu lệnh nào để in ra màn hình trong Python?", "options": ["print()", "echo()", "printf()", "display()"], "answer": "print()"},
    {"question": "Biến trong Python khai báo bằng từ khóa nào?", "options": ["var", "let", "const", "Không cần"], "answer": "Không cần"},
]


def load_question():
    global current_question, question_text
    new_question = choice(list)
    while new_question == current_question:
        new_question = choice(list)
        current_question = new_question
        question_text = current_question["list"]


buttons = []

for i, btn in enumerate(buttons):
    # global current_question
    # btn = PushButton(box, text="", grid=[i % 2, (i//2)+1], command=load_question, args=[i])
    buttons.append(btn)
    btn.text = current_question["options"][i]
    btn.enable()


def check_answer(index):
    """Kiểm tra đáp án và xử lý kết quả."""
    selected_option = current_question["options"][index]
    if selected_option == current_question["answer"]:
        buttons[index].bg = "#58D68D"  # Xanh khi đúng
        info("Kết quả", "🎉 Chính xác! Bạn đã trả lời đúng.")

        # Vô hiệu hóa tất cả các nút
        for btn in buttons:
            btn.disable()
        # load_question()
        app.after(500, load_question)  # Đổi câu hỏi sau 500ms
    else:
        buttons[index].bg = "#E74C3C"  # Đỏ khi sai
        info("Kết quả", "❌ Sai rồi! Hãy thử lại.")
        buttons[index].disable()


reload_button = PushButton(app, text="🔄 Câu hỏi khác", command=load_question)
current_question = None
question_text = Text(Box, text="", grid=[0, 0, 2, 1])
for i in range():
    btn = PushButton(box, text="", grid=[i % 2, (i//2)+1], command=load_question, args=[i])


load_question()
app.display()