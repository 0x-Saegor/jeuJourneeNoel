import tkinter as tk
from tkinter import messagebox
import socket
import threading
from customtkinter import *
              
#Fenetre côté joueur
window = CTk()
window.geometry("500x200")
window.resizable(width=False, height=False)
window.title("Client - Joueur")
username = " "

def testc():
    text = "Esse eu laborum sint labore eiusmod Lorem ad sint qui velit deserunt."
    text2 = text.split(" ")
    if len(text2) > 12:
        text2.insert(12, "\n")
    elif len(text2) > 6:
        text2.insert(6, "\n")
    final = " ".join(text2)
    print(final)
    rep_score.configure(text=final)
      
      
#Fenêtre côté spectateur
window2 = CTkToplevel()
window2.geometry("1920x1080")

topFrame = CTkFrame(window)
lblName = CTkLabel(topFrame, text = "Name:", font=CTkFont(size=20)).pack(side="left", padx=(5, 0))
entName = CTkEntry(topFrame)
entName.pack(side="left", padx=(5, 0))
btnConnect = CTkButton(topFrame, text="Connect", command=lambda : connect())
btnConnect.pack(side="left", padx=(5, 0))

#btnConnect.bind('<Button-1>', connect)
topFrame.pack(side="top", fill="x", expand=True)

displayFrame = CTkFrame(window)
reponseA = CTkButton(displayFrame, text="A", command=lambda : answer_A())
#reponseA.pack(side="left")
reponseB = CTkButton(displayFrame, text="B", command=lambda : answer_B())
#reponseB.pack(side="left")
reponseC = CTkButton(displayFrame, text="C", command=lambda : answer_C())
#reponseA.pack(side="left")
reponseD = CTkButton(displayFrame, text="D", command=lambda : answer_D())
#reponseD.pack(side="left")

displayFrame.pack(side="top", fill="x", expand=True)


affichage=CTkFrame(window2, width=1920, height=1080)

nom_joueur = CTkLabel(affichage, text ="", font=CTkFont(size=50))
nom_joueur.pack(side="top", pady=5, padx=5)

rep_score = CTkLabel(affichage, text ="", font=CTkFont(size=75), width=1920, height=1080)
rep_score.pack(side="top", pady=5, padx=5)


affichage.pack(side="top")


'''
lblLine = tk.Label(displayFrame, text="*********************************************************************").pack()
scrollBar = tk.Scrollbar(displayFrame)
scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
tkDisplay = tk.Text(displayFrame, height=20, width=55)
tkDisplay.pack(side="left", fill=tk.Y, padx=(5, 0))
tkDisplay.tag_config("tag_your_message", foreground="blue")
scrollBar.configure(command=tkDisplay.yview)
tkDisplay.configure(yscrollcommand=scrollBar.set, background="#F4F6F7", highlightbackground="grey", state="disabled")
displayFrame.pack(side="top")
'''
bottomFrame = CTkFrame(window)
tkMessage = CTkTextbox(bottomFrame, height=2, width=55)

tkMessage.configure(state="disabled")
tkMessage.bind("<Return>", (lambda event: getChatMessage(tkMessage.get("1.0", "end"))))
bottomFrame.pack(side="bottom", fill="x", expand=True)

def answer_A():
      global client
      reponse=reponseA.cget('text')
      reponseA.pack_forget()
      reponseB.pack_forget()
      reponseC.pack_forget()
      reponseD.pack_forget()
      client.send(reponse.encode())

def answer_B():
      global client
      reponse=reponseB.cget('text')
      reponseA.pack_forget()
      reponseB.pack_forget()
      reponseC.pack_forget()
      reponseD.pack_forget()
      client.send(reponse.encode())

def answer_C():
      global client
      reponse=reponseC.cget('text')
      reponseA.pack_forget()
      reponseB.pack_forget()
      reponseC.pack_forget()
      reponseD.pack_forget()
      client.send(reponse.encode())

def answer_D():
      global client
      reponse=reponseD.cget('text')
      reponseA.pack_forget()
      reponseB.pack_forget()
      reponseC.pack_forget()
      reponseD.pack_forget()
      client.send(reponse.encode())

def connect():
    global username, client,nom_joueur
    if len(entName.get()) < 1:
        messagebox.showerror(title="ERROR!!!", message="You MUST enter your first name <e.g. John>")
    else:
        username = entName.get()
        nom_joueur.configure(text=username)
        connect_to_server(username)


# network client
client = None
HOST_ADDR = "127.0.0.1"
HOST_PORT = 59000

def connect_to_server(name):
    global client, HOST_PORT, HOST_ADDR
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST_ADDR, HOST_PORT))
        client.send(name.encode()) # Send name to server after connecting

        entName.configure(state="disabled")
        btnConnect.configure(state="disabled")
        tkMessage.configure(state="normal")

        # start a thread to keep receiving message from server
        # do not block the main thread :)
        threading._start_new_thread(receive_message_from_server, (client, "m"))
    except Exception as e:
        messagebox.showerror(title="ERROR!!!", message="Cannot connect to host: " + HOST_ADDR + " on port: " + str(HOST_PORT) + " Server may be Unavailable. Try again later")


def receive_message_from_server(sck, m):
    global client
    while True:
        from_server = sck.recv(4096).decode()
        rep_score.configure(text="")
        tab=from_server.split(";")
        print(tab)
        if not from_server: break
        
        # display message from server on the chat window
            
        # enable the display area and insert the text and then disable.
        # why? Apparently, tkinter does not allow us insert into a disabled Text widget :(
        #texts = tkDisplay.get("1.0", "end").strip()
        #tkDisplay.configure(state="normal")
        if tab[0]=="Duo":
                        #afficher les deux réponses dans deux boutons
                        reponseA.configure(text = tab[2])
                        reponseA.pack(side="left", pady=5, padx=5)
                        reponseB.configure(text = tab[4])
                        reponseB.pack(side="left", pady=5, padx=5)
                        print(tab)
        elif tab[0]=="Carré":
                        #afficher les quatres propositions dans les quatres boutons
                        reponseA.configure(text = tab[2])
                        reponseA.pack(side="left", pady=5, padx=5)
                        reponseB.configure(text = tab[4])
                        reponseB.pack(side="left", pady=5, padx=5)
                        reponseC.configure(text = tab[6])
                        reponseC.pack(side="left", pady=5, padx=5)
                        reponseD.configure(text = tab[8])
                        reponseD.pack(side="left", pady=5, padx=5)
                        print(tab)
        elif tab[0]=="Cash":
                        tkMessage.pack(side="left", padx=(5, 13), pady=(5, 10))
                        print("question cash")
        elif tab[0]=='reponse':
              
               rep_score.configure(text=tab[1], font=CTkFont(size=100))
               
        elif tab[0]=='score':
               
               rep_score.configure(text=tab[1], font=CTkFont(size=150))
               
        elif tab[0]=='eliminate':
            window.destroy()
        #tkDisplay.configure(state="disabled")
        #tkDisplay.see("end")

    print("Server says: " +from_server)
    print(tab)

    sck.close()
    window.destroy()

def getChatMessage(msg):

    msg = msg.replace('\n', '')


    send_mssage_to_server(msg)

    tkMessage.delete('1.0', "end")
    tkMessage.pack_forget()


def send_mssage_to_server(msg):
    client_msg = str(msg)
    client.send(client_msg.encode())
    if msg == "exit":
        client.close()
        window.destroy()
    print("Sending message")


window.mainloop()
