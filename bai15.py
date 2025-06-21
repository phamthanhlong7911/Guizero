with open("exp.txt", "w", encoding="utf-8") as f:
    f.write("\n chúc thầy học tốt")
with open("exp.txt", "r", encoding="utf-8") as f:
    x = f.read()
with open("exp.txt", "a", encoding="utf-8") as f:
    f.write("\n chúc thầy học ko tốt")
with open("exp.txt", "r", encoding="utf-8") as f:
    x = f.read()
    print(x)