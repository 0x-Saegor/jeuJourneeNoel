from customtkinter import *

app = CTk()
app.title("Player")
app.geometry("800x600")
app.resizable(False, False)

def load_questions():
    questions = []
    with open("questions.csv", "r", encoding="utf-8") as file:
        # skip the first line
        f = file.readlines()
        for line in f:
            questions.append(line.split(";"))
    return questions

questions = load_questions()
        

title_question = CTkLabel(app, text=f"Question : {questions[1][2]}", font=CTkFont(size=16, weight="bold"))
title_question.grid(row=0, column=0, padx=20, pady=(20, 10))

first_prop = CTkButton(app, text=f"1. {questions[1][3]}", font=CTkFont(size=16))
first_prop.grid(row=1, column=0, padx=20, pady=(20, 10))

sec_prop = CTkButton(app, text=f"2. {questions[1][4]}", font=CTkFont(size=16))
sec_prop.grid(row=2, column=0, padx=20, pady=(20, 10))

        


app.mainloop()