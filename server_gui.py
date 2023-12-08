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
def charger_emission(fichier):
    global questions
    questions=extractionDonnees(fichier,";")
    print(questions)

window = tk.Tk()
window.title("Serveur")

# Top frame consisting of two buttons widgets (i.e. btnStart, btnStop)
topFrame = tk.Frame(window)
btnStart = tk.Button(topFrame, text="Connect", command=lambda : start_server())
btnStart.pack(side=tk.LEFT)
btnStop = tk.Button(topFrame, text="Stop", command=lambda : stop_server(), state=tk.DISABLED)
btnStop.pack(side=tk.LEFT)

charge_emission=tk.Button(topFrame, text="Emission 1", command=lambda : charger_emission("questions.csv") )
charge_emission.pack(side=tk.RIGHT)

envoi=tk.Button(topFrame, text="Connect", command=lambda : envoi_reponse())
envoi.pack(side=tk.RIGHT)
topFrame.pack(side=tk.TOP, pady=(5, 0))

# Middle frame consisting of two labels for displaying the host and port info
middleFrame = tk.Frame(window)
lblHost = tk.Label(middleFrame, text = "Host: X.X.X.X")
lblHost.pack(side=tk.LEFT)
lblPort = tk.Label(middleFrame, text = "Port:XXXX")
lblPort.pack(side=tk.LEFT)
middleFrame.pack(side=tk.TOP, pady=(5, 0))

# The client frame shows the client area
cadre_J1 = tk.Frame(window)
joueur1_display = tk.Text(cadre_J1, height=15, width=30)
joueur1_display.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 0))
cadre_J1.pack(side=tk.BOTTOM, pady=(5, 10))

cadre_J2 = tk.Frame(window)
joueur2_display = tk.Text(cadre_J2, height=15, width=30)
joueur2_display.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 0))
cadre_J2.pack(side=tk.BOTTOM, pady=(5, 10))

cadre_J3 = tk.Frame(window)
joueur3_display = tk.Text(cadre_J3, height=15, width=30)
joueur3_display.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 0))
cadre_J3.pack(side=tk.BOTTOM, pady=(5, 10))


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
        joueurs[sending_client_name][0].config(state=tk.NORMAL)
        joueurs[sending_client_name].append(client_connection)
        joueurs[sending_client_name].append(client_msg)
        joueurs[sending_client_name][0].insert(tk.END, "\n"+sending_client_name+ "a dit "+client_msg)
        joueurs[sending_client_name][0].config(state=tk.DISABLED)
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

def envoi_reponse():
    global clients, joueurs
    for joueur in joueurs:
                print(joueur[1],type(joueurs[joueur][1]))
                reponse_joueur = joueurs[joueur][2]
                joueurs[joueur][1].send(reponse_joueur.encode())


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
    affichage=[joueur1_display,joueur2_display]
    for i in range (len(name_list)):
        joueurs[name_list[i]]=[]
        joueurs[name_list[i]].append(affichage[i])
    print(joueurs)


            
window.mainloop()