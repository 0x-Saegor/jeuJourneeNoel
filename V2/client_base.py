import tkinter as tk
from tkinter import messagebox
import socket
import threading

class Extra(tk.Toplevel):
	def __init__(self):
		super().__init__()
		self.title('Client - Joueur')
		self.geometry('300x400')
              
#Fenetre côté joueur
window = tk.Tk()
window.geometry("500x200")
window.title("Client - Joueur")
username = " "

#Fenêtre côté spectateur
window2 = Extra()


topFrame = tk.Frame(window)
lblName = tk.Label(topFrame, text = "Name:").pack(side=tk.LEFT)
entName = tk.Entry(topFrame)
entName.pack(side=tk.LEFT)
btnConnect = tk.Button(topFrame, text="Connect", command=lambda : connect())
btnConnect.pack(side=tk.LEFT)
#btnConnect.bind('<Button-1>', connect)
topFrame.pack(side=tk.TOP)

displayFrame = tk.Frame(window)
reponseA = tk.Button(displayFrame, text="A", command=lambda : answer_A())
#reponseA.pack(side=tk.LEFT)
reponseB = tk.Button(displayFrame, text="B", command=lambda : answer_B())
#reponseB.pack(side=tk.LEFT)
reponseC = tk.Button(displayFrame, text="C", command=lambda : answer_C())
#reponseA.pack(side=tk.LEFT)
reponseD = tk.Button(displayFrame, text="D", command=lambda : answer_D())
#reponseB.pack(side=tk.LEFT)

displayFrame.pack(side=tk.TOP)


affichage=tk.Frame(window2)

nom_joueur = tk.Label(affichage, text ="")
nom_joueur.pack(side=tk.TOP)

affiche_rep=tk.Text(affichage, height=15, width=30)
affiche_rep.pack(side=tk.TOP, fill=tk.Y, padx=(5, 0))
affichage.pack(side=tk.TOP)


'''
lblLine = tk.Label(displayFrame, text="*********************************************************************").pack()
scrollBar = tk.Scrollbar(displayFrame)
scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
tkDisplay = tk.Text(displayFrame, height=20, width=55)
tkDisplay.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 0))
tkDisplay.tag_config("tag_your_message", foreground="blue")
scrollBar.config(command=tkDisplay.yview)
tkDisplay.config(yscrollcommand=scrollBar.set, background="#F4F6F7", highlightbackground="grey", state="disabled")
displayFrame.pack(side=tk.TOP)
'''
bottomFrame = tk.Frame(window)
tkMessage = tk.Text(bottomFrame, height=2, width=55)

tkMessage.config(highlightbackground="grey", state="disabled")
tkMessage.bind("<Return>", (lambda event: getChatMessage(tkMessage.get("1.0", tk.END))))
bottomFrame.pack(side=tk.BOTTOM)

def answer_A():
      global client
      reponse=reponseA['text']
      reponseA.pack_forget()
      reponseB.pack_forget()
      reponseC.pack_forget()
      reponseD.pack_forget()
      client.send(reponse.encode())

def answer_B():
      global client
      reponse=reponseB['text']
      reponseA.pack_forget()
      reponseB.pack_forget()
      reponseC.pack_forget()
      reponseD.pack_forget()
      client.send(reponse.encode())

def answer_C():
      global client
      reponse=reponseC['text']
      reponseA.pack_forget()
      reponseB.pack_forget()
      reponseC.pack_forget()
      reponseD.pack_forget()
      client.send(reponse.encode())

def answer_D():
      global client
      reponse=reponseD['text']
      reponseA.pack_forget()
      reponseB.pack_forget()
      reponseC.pack_forget()
      reponseD.pack_forget()
      client.send(reponse.encode())

def connect():
    global username, client,nom_joueur
    if len(entName.get()) < 1:
        tk.messagebox.showerror(title="ERROR!!!", message="You MUST enter your first name <e.g. John>")
    else:
        username = entName.get()
        nom_joueur['text']=username
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

        entName.config(state=tk.DISABLED)
        btnConnect.config(state=tk.DISABLED)
        tkMessage.config(state=tk.NORMAL)

        # start a thread to keep receiving message from server
        # do not block the main thread :)
        threading._start_new_thread(receive_message_from_server, (client, "m"))
    except Exception as e:
        tk.messagebox.showerror(title="ERROR!!!", message="Cannot connect to host: " + HOST_ADDR + " on port: " + str(HOST_PORT) + " Server may be Unavailable. Try again later")


def receive_message_from_server(sck, m):
    global client
    while True:
        from_server = sck.recv(4096).decode()
        affiche_rep.delete('1.0', 'end')
        tab=from_server.split(";")
        print(tab)
        if not from_server: break
        
        # display message from server on the chat window
            
        # enable the display area and insert the text and then disable.
        # why? Apparently, tkinter does not allow us insert into a disabled Text widget :(
        #texts = tkDisplay.get("1.0", tk.END).strip()
        #tkDisplay.config(state=tk.NORMAL)
        if tab[0]=="Duo":
                        #afficher les deux réponses dans deux boutons
                        reponseA['text']=tab[2]
                        reponseA.pack(side=tk.LEFT)
                        reponseB['text']=tab[4]
                        reponseB.pack(side=tk.LEFT)
                        print(tab)
        elif tab[0]=="Carré":
                        #afficher les quatres propositions dans les quatres boutons
                        reponseA['text']=tab[2]
                        reponseA.pack(side=tk.LEFT)
                        reponseB['text']=tab[4]
                        reponseB.pack(side=tk.LEFT)
                        reponseC['text']=tab[6]
                        reponseC.pack(side=tk.LEFT)
                        reponseD['text']=tab[8]
                        reponseD.pack(side=tk.LEFT)
                        print(tab)
        elif tab[0]=="Cash":
                        tkMessage.pack(side=tk.LEFT, padx=(5, 13), pady=(5, 10))
                        print("question cash")
        elif tab[0]=='reponse':
              
               affiche_rep.insert(tk.END, tab[1])
               affiche_rep.config(state=tk.NORMAL)
        elif tab[0]=='score':
               
               affiche_rep.insert(tk.END, tab[1])
               affiche_rep.config(state=tk.NORMAL)
        #tkDisplay.config(state=tk.DISABLED)
        #tkDisplay.see(tk.END)

       #print("Server says: " +from_server)

    sck.close()
    window.destroy()

def getChatMessage(msg):

    msg = msg.replace('\n', '')


    send_mssage_to_server(msg)

    tkMessage.delete('1.0', tk.END)
    tkMessage.pack_forget()


def send_mssage_to_server(msg):
    client_msg = str(msg)
    client.send(client_msg.encode())
    if msg == "exit":
        client.close()
        window.destroy()
    print("Sending message")


window.mainloop()
