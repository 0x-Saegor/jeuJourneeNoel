from customtkinter import *

app = CTk()
app.title("Player")
app.geometry("600x675")
app.resizable(False, False)

"""self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="CustomTkinter", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))"""

### Functions ###


def ready():
    btn.configure(state="disabled")
    text.configure(text="Choisissez une réponse")
    answer_A.configure(state="normal")
    answer_B.configure(state="normal")
    answer_C.configure(state="normal")
    answer_D.configure(state="normal")
    text_second.configure(text="En cours de réponse...")


def clicked(answer):
    answer_A.configure(state="disabled")
    answer_B.configure(state="disabled")
    answer_C.configure(state="disabled")
    answer_D.configure(state="disabled")
    btn.configure(state="normal")
    text_second.configure(text="Le joueur a choisi la réponse : " + answer)
    text.configure(text="J'ai lu et je suis prêt à valider (définitif)")

### Top Frame ###


text = CTkLabel(
    app, text="J'ai lu et je suis prêt à valider (définitif)", font=CTkFont(size=20))
text.pack(fill="both", expand=True)

btn = CTkButton(app, text="Prêt", command=ready)
btn.pack(pady=20)

### Content Frame ###

buttonsFrame = CTkFrame(app, corner_radius=0)
buttonsFrame.pack(fill="both", expand=True)
buttonsFrame.grid_columnconfigure(2, weight=100)
buttonsFrame.grid_rowconfigure(2, weight=100)

answer_A = CTkButton(buttonsFrame, text="A", command=lambda: clicked(
    "A"), width=250, height=250, font=CTkFont(size=40), state="disabled")
answer_A.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

answer_B = CTkButton(buttonsFrame, text="B", command=lambda: clicked(
    "B"), width=250, height=250, font=CTkFont(size=40), state="disabled")
answer_B.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

answer_C = CTkButton(buttonsFrame, text="C", command=lambda: clicked(
    "B"), width=250, height=250, font=CTkFont(size=40), state="disabled")
answer_C.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)

answer_D = CTkButton(buttonsFrame, text="D", command=lambda: clicked(
    "B"), width=250, height=250, font=CTkFont(size=40), state="disabled")
answer_D.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)

### Second windows ###

window = CTkToplevel(app)
window.geometry("1920x1080")


text_second = CTkLabel(
    window, text="Pas de réponse choisie...", font=CTkFont(size=40))
text_second.pack(fill="both", expand=True)


app.mainloop()
