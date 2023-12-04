# fais une feneêtre sous customtkinter
from customtkinter import *

app = CTk()
app.title("Admin")
app.geometry("800x600")
app.resizable(False, False)

# Grid on the left to add points to each of 5 players

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

app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure((2, 3), weight=0)
app.grid_rowconfigure((0, 1, 2), weight=1)

## Frames ###
# create a sidebar frame with a label : "Ajouter des points" and a button "Ajouter" to each player,
sidebar = CTkFrame(app, width=140, corner_radius=0)
sidebar.grid(row=0, column=0, rowspan=4, sticky="nsew")
sidebar.grid_rowconfigure(4, weight=1)
logo_label = CTkLabel(sidebar, text="Ajouter des points", font=CTkFont(size=17, weight="bold"))
logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

player1 = CTkFrame(sidebar, width=140, corner_radius=0)
player1.grid(row=1, column=0, sticky="nsew")
player1.grid_rowconfigure(4, weight=1)
player1_label = CTkLabel(player1, text="Joueur 1", font=CTkFont(size=20, weight="bold"))
player1_label.grid(row=0, column=0, padx=20, pady=(20, 10))
player1_button = CTkButton(player1, text="Ajouter")
player1_button.grid(row=1, column=0, padx=20, pady=10)

player2 = CTkFrame(sidebar, width=140, corner_radius=0)
player2.grid(row=2, column=0, sticky="nsew")
player2.grid_rowconfigure(4, weight=1)
player2_label = CTkLabel(player2, text="Joueur 2", font=CTkFont(size=20, weight="bold"))
player2_label.grid(row=0, column=0, padx=20, pady=(20, 10))
player2_button = CTkButton(player2, text="Ajouter")
player2_button.grid(row=1, column=0, padx=20, pady=10)

player3 = CTkFrame(sidebar, width=140, corner_radius=0)
player3.grid(row=3, column=0, sticky="nsew")
player3.grid_rowconfigure(4, weight=1)
player3_label = CTkLabel(player3, text="Joueur 3", font=CTkFont(size=20, weight="bold"))
player3_label.grid(row=0, column=0, padx=20, pady=(20, 10))
player3_button = CTkButton(player3, text="Ajouter")
player3_button.grid(row=1, column=0, padx=20, pady=10)

player4 = CTkFrame(sidebar, width=140, corner_radius=0)
player4.grid(row=4, column=0, sticky="nsew")
player4.grid_rowconfigure(4, weight=1)
player4_label = CTkLabel(player4, text="Joueur 4", font=CTkFont(size=20, weight="bold"))
player4_label.grid(row=0, column=0, padx=20, pady=(20, 10))
player4_button = CTkButton(player4, text="Ajouter")
player4_button.grid(row=1, column=0, padx=20, pady=10)

player5 = CTkFrame(sidebar, width=140, corner_radius=0)
player5.grid(row=5, column=0, sticky="nsew")
player5.grid_rowconfigure(4, weight=1)
player5_label = CTkLabel(player5, text="Joueur 5", font=CTkFont(size=20, weight="bold"))
player5_label.grid(row=0, column=0, padx=20, pady=(20, 10))
player5_button = CTkButton(player5, text="Ajouter")
player5_button.grid(row=1, column=0, padx=20, pady=10)

### Main Frame ###
main_frame = CTkFrame(app, corner_radius=0)
main_frame.grid(row=0, column=1, rowspan=4, sticky="nsew")
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_rowconfigure(0, weight=1)

# Ajouter un bouton question suivante et un bouton afficher la réponse

# Frame buttons
buttonsFrame = CTkFrame(main_frame, corner_radius=0)
buttonsFrame.pack(fill="both", expand=True, padx=20, pady=20)


buttonQuestion = CTkButton(buttonsFrame, text="Question suivante", width=250)
buttonQuestion.pack(pady=40)

buttonAnswer = CTkButton(buttonsFrame, text="Afficher la réponse", width=250)
buttonAnswer.pack()




app.mainloop()