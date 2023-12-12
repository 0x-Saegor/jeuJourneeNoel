import tkinter as tk
import socket
import threading
import csv


def extractionDonnees(nomFichier,separateur):
    '''
    précondition : nomFichier est du type str et doit être le nom d'un fichier csv.
                   separateur est de type str et doit être soit une virgule ou un point virgule.
    postcondition: Cette fonction récupère les données d'un fichier csv et renvoie un tableau contenant
    des dictionnaires dont les clés sont les descripteurs associés :
    La liste des descripteurs et la liste de toutes les données
    '''
    if nomFichier[-4:]!=".csv":
        return "Erreur : Ce fichier n'est pas un fichier CSV"
    else :
        tab=[]
        with open(nomFichier, newline='',encoding='utf-8-sig') as csvfile:
            fichier = csv.DictReader(csvfile, delimiter=separateur)
    # pour remplir notre tableau, une boucle for parcourant chaque ligne du fichier csv sera utilisée
            for ligne in fichier :
                tab.append(dict(ligne))
        return tab

questions={}
joueurs={}
indice=0

def charger_emission(fichier):
    global questions
    questions=extractionDonnees(fichier,";")
    print(questions)

window = tk.Tk()
window.title("Serveur")
window.geometry("500x500")

# boutons démarrage et arrêt du serveur
topFrame = tk.Frame(window)
btnStart = tk.Button(topFrame, text="Connect", command=lambda : start_server())
btnStart.pack(side=tk.LEFT)
btnStop = tk.Button(topFrame, text="Stop", command=lambda : stop_server(), state=tk.DISABLED)
btnStop.pack(side=tk.LEFT)

#bouton pour charger les émissions (il en faut 5)
charge_emission=tk.Button(topFrame, text="Emission 1", command=lambda : charger_emission("questions.csv") )
charge_emission.pack(side=tk.RIGHT)

#boutons pour envoyer des infos aux clients (propositions ou score - il manque le bouton envoi_score)
envoi=tk.Button(topFrame, text="envoi", command=lambda : envoi_question())
envoi.pack(side=tk.RIGHT)

envoi_rep=tk.Button(topFrame, text="affiche réponse", command=lambda : envoi_reponse())
envoi_rep.pack(side=tk.RIGHT)

envoi_score=tk.Button(topFrame, text="affiche score", command=lambda : envoi_score())
envoi_score.pack(side=tk.RIGHT)
#bouton suivant pour passer à la question suivante
suivant=tk.Button(topFrame, text="Quest.Suivante", command=lambda : next())
suivant.pack(side=tk.RIGHT)
topFrame.pack(side=tk.TOP, pady=(5, 0))

# Affichage des infos de connexions
middleFrame = tk.Frame(window)
lblHost = tk.Label(middleFrame, text = "Host: X.X.X.X")
lblHost.pack(side=tk.LEFT)
lblPort = tk.Label(middleFrame, text = "Port:XXXX")
lblPort.pack(side=tk.LEFT)
middleFrame.pack(side=tk.TOP, pady=(5, 0))

#fenêtre J1
cadre_J1 = tk.Frame(window)
joueur1_display = tk.Text(cadre_J1, height=5, width=30)
joueur1_display.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 0))
cadre_J1.pack(side=tk.TOP, pady=(5, 5))

# boutons score J1
j1_1=tk.Button(cadre_J1, text="+1", command=lambda : plus_un_j1())
j1_1.pack(side=tk.BOTTOM)

j1_3=tk.Button(cadre_J1, text="+3", command=lambda : plus_trois_j1())
j1_3.pack(side=tk.BOTTOM)

j1_5=tk.Button(cadre_J1, text="+5", command=lambda : plus_cinq_j1())
j1_5.pack(side=tk.BOTTOM)

#fenêtre J2
cadre_J2 = tk.Frame(window)
joueur2_display = tk.Text(cadre_J2, height=5, width=30)
joueur2_display.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 0))
cadre_J2.pack(side=tk.TOP, pady=(5, 5))

# boutons score J2
j2_1=tk.Button(cadre_J2, text="+1", command=lambda : plus_un_j2())
j2_1.pack(side=tk.BOTTOM)

j2_3=tk.Button(cadre_J2, text="+3", command=lambda : plus_trois_j2())
j2_3.pack(side=tk.BOTTOM)

j2_5=tk.Button(cadre_J2, text="+5", command=lambda : plus_cinq_j2())
j2_5.pack(side=tk.BOTTOM)

#fenêtre J3
cadre_J3 = tk.Frame(window)
joueur3_display = tk.Text(cadre_J3, height=5, width=30)
joueur3_display.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 0))
cadre_J3.pack(side=tk.TOP, pady=(5, 5))

# boutons score J3
j3_1=tk.Button(cadre_J3, text="+1", command=lambda : plus_un_j3())
j3_1.pack(side=tk.BOTTOM)

j3_3=tk.Button(cadre_J3, text="+3", command=lambda : plus_trois_j3())
j3_3.pack(side=tk.BOTTOM)

j3_5=tk.Button(cadre_J3, text="+5", command=lambda : plus_cinq_j3())
j3_5.pack(side=tk.BOTTOM)

#fenêtre J4
cadre_J4 = tk.Frame(window)
joueur4_display = tk.Text(cadre_J4, height=5, width=30)
joueur4_display.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 0))
cadre_J4.pack(side=tk.TOP, pady=(5, 5))

# boutons score J4
j4_1=tk.Button(cadre_J4, text="+1", command=lambda : plus_un_j4())
j4_1.pack(side=tk.BOTTOM)

j4_3=tk.Button(cadre_J4, text="+3", command=lambda : plus_trois_j4())
j4_3.pack(side=tk.BOTTOM)

j4_5=tk.Button(cadre_J4, text="+5", command=lambda : plus_cinq_j4())
j4_5.pack(side=tk.BOTTOM)

#fenêtre J5
cadre_J5 = tk.Frame(window)
joueur5_display = tk.Text(cadre_J5, height=5, width=30)
joueur5_display.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 0))
cadre_J5.pack(side=tk.TOP, pady=(5, 5))

# boutons score J5
j5_1=tk.Button(cadre_J5, text="+1", command=lambda : plus_un_j5())
j5_1.pack(side=tk.BOTTOM)

j5_3=tk.Button(cadre_J5, text="+3", command=lambda : plus_trois_j5())
j5_3.pack(side=tk.BOTTOM)

j5_5=tk.Button(cadre_J5, text="+5", command=lambda : plus_cinq_j5())
j5_5.pack(side=tk.BOTTOM)
###################################################################
server = None
HOST_ADDR = "127.0.0.1"
HOST_PORT = 59000
client_name = " "
clients = []
clients_names = []


# Start server function
def start_server():
    global server, HOST_ADDR, HOST_PORT # code is fine without this
    btnStart.config(state=tk.DISABLED)
    btnStop.config(state=tk.NORMAL)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(socket.AF_INET)
    print(socket.SOCK_STREAM)

    server.bind((HOST_ADDR, HOST_PORT))
    server.listen(5)  # server is listening for client connection

    threading._start_new_thread(accept_clients, (server, " "))

    lblHost["text"] = "Host: " + HOST_ADDR
    lblPort["text"] = "Port: " + str(HOST_PORT)


# Stop server function
def stop_server():
    global server
    btnStart.config(state=tk.NORMAL)
    btnStop.config(state=tk.DISABLED)


def accept_clients(the_server, y):
    while True:
        client, addr = the_server.accept()
        clients.append(client)

        # use a thread so as not to clog the gui thread
        threading._start_new_thread(send_receive_client_message, (client, addr))


# Function to receive message from current client AND
# Send that message to other clients
def send_receive_client_message(client_connection, client_ip_addr):
    global server, client_name, clients, clients_addr,joueurs
    client_msg = " "

    # send welcome message to client
    client_name  = client_connection.recv(4096).decode()
    joueurs[client_name]={}
    joueurs[client_name]['socket']=client_connection

    welcome_msg = "Welcome " + client_name + ". Use 'exit' to quit"
    client_connection.send(welcome_msg.encode())

    clients_names.append(client_name)

    update_client_names_display(clients_names)  # update client names display


    while True:
        data = client_connection.recv(4096).decode()
        if not data: break
        if data == "exit": break

        client_msg = data
       
        idx = get_client_index(clients, client_connection)
        sending_client_name = clients_names[idx]
        joueurs[sending_client_name]['affichage'].config(state=tk.NORMAL)
        
        joueurs[sending_client_name]['message']=client_msg
        joueurs[sending_client_name]['affichage'].insert(tk.END, "\n"+sending_client_name+ " a dit "+client_msg)
        joueurs[sending_client_name]['affichage'].config(state=tk.DISABLED)
        print(joueurs)
        #for c in clients:
        #   if c != client_connection:
        #       server_msg = str(client_msg)
        #       c.send(server_msg.encode())
    
    # find the client index then remove from both lists(client name list and connection list)
    idx = get_client_index(clients, client_connection)
    del clients_names[idx]
    del clients[idx]
    server_msg = "BYE!"
    client_connection.send(server_msg.encode())
    client_connection.close()

    update_client_names_display(clients_names)  # update client names display



def envoi_question():
    global questions,joueurs,indice
    print(questions[indice]['A'],questions[indice]['B'])
    for joueur in joueurs :
        match questions[indice]["Type"]:
            case "Duo":
                question=str(questions[indice]["Type"]+";A;"+questions[indice]['A']+";B;"+questions[indice]['B'])
            case "Carré":
                question=str(questions[indice]["Type"]+";A;"+questions[indice]['A']+";B;"+questions[indice]['B']+";C;"+questions[indice]['C']+";D;"+questions[indice]['D'])
            case "Cash":
                question=str(questions[indice]["Type"])
        print(question[0:7])
        joueurs[joueur]['socket'].send(question.encode())



def envoi_reponse():
    global clients, joueurs
    for joueur in joueurs:
                print(type(joueurs[joueur]['message']))
                reponse_joueur = joueurs[joueur]['message']
                joueurs[joueur]['socket'].send(("reponse;"+reponse_joueur).encode())


def envoi_score():
    global clients, joueurs
    for joueur in joueurs:
                print(type(joueurs[joueur]['score']))
                score_joueur = joueurs[joueur]['score']
                joueurs[joueur]['socket'].send(("score;"+str(score_joueur)).encode())
def next():
    global indice
    indice+=1
    return indice

############################# Score du joueur 1 #################################
def plus_un_j1():
     global joueurs,clients_names
     joueurs[clients_names[0]]['score']+=1
     print(joueurs)

def plus_trois_j1():
     global joueurs,clients_names
     joueurs[clients_names[0]]['score']+=3
     print(joueurs)

def plus_cinq_j1():
     global joueurs,clients_names
     joueurs[clients_names[0]]['score']+=5
     print(joueurs)

############################# Score du joueur 2 #################################
def plus_un_j2():
     global joueurs,clients_names
     joueurs[clients_names[1]]['score']+=1
     print(joueurs)

def plus_trois_j2():
     global joueurs,clients_names
     joueurs[clients_names[1]]['score']+=3
     print(joueurs)

def plus_cinq_j2():
     global joueurs,clients_names
     joueurs[clients_names[1]]['score']+=5
     print(joueurs)

############################# Score du joueur 3 #################################
def plus_un_j3():
     global joueurs,clients_names
     joueurs[clients_names[2]]['score']+=1
     print(joueurs)

def plus_trois_j3():
     global joueurs,clients_names
     joueurs[clients_names[2]]['score']+=3
     print(joueurs)

def plus_cinq_j3():
     global joueurs,clients_names
     joueurs[clients_names[2]]['score']+=5
     print(joueurs)

############################# Score du joueur 4 #################################
def plus_un_j4():
     global joueurs,clients_names
     joueurs[clients_names[3]]['score']+=1
     print(joueurs)

def plus_trois_j4():
     global joueurs,clients_names
     joueurs[clients_names[3]]['score']+=3
     print(joueurs)

def plus_cinq_j4():
     global joueurs,clients_names
     joueurs[clients_names[3]]['score']+=5
     print(joueurs)


############################# Score du joueur 5 #################################
def plus_un_j5():
     global joueurs,clients_names
     joueurs[clients_names[4]]['score']+=1
     print(joueurs)

def plus_trois_j5():
     global joueurs,clients_names
     joueurs[clients_names[4]]['score']+=3
     print(joueurs)

def plus_cinq_j5():
     global joueurs,clients_names
     joueurs[clients_names[4]]['score']+=5
     print(joueurs)

# Return the index of the current client in the list of clients
def get_client_index(client_list, curr_client):
    idx = 0
    for conn in client_list:
        if conn == curr_client:
            break
        idx = idx + 1

    return idx


# Update client name display when a new client connects OR
# When a connected client disconnects

def update_client_names_display(name_list):
    global joueurs
    affichage=[joueur1_display,joueur2_display,joueur3_display,joueur4_display,joueur5_display]
    for i in range (len(name_list)):
       
        joueurs[name_list[i]]['affichage']=affichage[i]
        joueurs[name_list[i]]['score']=0
    print(joueurs)


            
window.mainloop()
