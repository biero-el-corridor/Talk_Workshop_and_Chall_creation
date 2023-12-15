import socket

def handle_connection(client_socket, question, correct_answer):
    client_socket.sendall(question.encode())
    response = client_socket.recv(1024).decode()
    
    if response.lower().strip() == correct_answer.lower().strip():
        client_socket.sendall("Bonne réponse!\n".encode())
        return True
    else:
        client_socket.sendall("Réponse incorrecte. La connexion se termine.\n".encode())
        return False

def main():
    host = '0.0.0.0'
    port = 56789  # Port is modified to 56789

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Attente de connexions sur le port {port}...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connexion établie avec {addr} , les élément entre () sont le format de flag x correspond a une minuscule X correspond a une majuscule. La taille du format ne correspond pas toujour a la taille des flag, il y a une quinzaine de questions")

        # Updated questions and answers
        questions = ["Quelle est l'IP de la machine attaquante ? (X.X.X.X)"
        , "Quel est l'ip de la machine attaquante ? (X.X.X.X)"
        , "C'est surement nmap qu'il a utiliser pour faire de la reconaissence , quelle type de scan a til effectuer ? (-xX)",
        "ok super , il a donc constater que le port 102 etais up, il a dut utiliser un outils pour cominiquer via le port 102, quelle outil a t'il surement utiliser ? (xxxxxxX)",
        "quelle emplacement mémoire a t'il scanner au moin 3 fois. (XXX.X,XXX.X,XXX.X)",
        "quelle emplacement mémoire a vue le plus de voie sa valeur modifier ? (XXX.X)",
        "super , on sais comment il a pus étre ausi rapide , nous n'avion pas détecter la phase de reconaisence, (taper \"entrer\" pour passer a la suite.)",
        "il n'est donc pas passer par snap7 pour écrire les adresse memoire , donner le code mitre de la TTP qui a permie la phase d'exploitations",
        "donner le 14 éme \"Security hint\" de connexions", 
        "donner le \"Security hint\" qui a permie la connexions",
        "quelle et la versions du firmware du LOGO! ? ",
        "quelle variable on étée ajouter au dashobard ?", 
        "quelle sont les statue fineaux des variable ? (X.X.X.X.X)", 
        "combien de temps (arrondie a la moitié de minute) a durée l'attaque (entre le début du nmap et la déconnexions de l'attaquant) ? (XX.XX)",
        "GG weel played , contact biero sur discord, il te donneras le "]
        
        answers = ["10.1.2.7", "10.1.1.15","-sS","snap7","V1064.0,V1064.1,V1064.2,V1064.3,V1064.4","V1064.2","T1110","","","","",""]

        connection_successful = True

        for i, question in enumerate(questions):
            if not handle_connection(client_socket, f"Question {i+1}: {question}\nRéponse: ", answers[i]):
                connection_successful = False
                break
        client_socket.close()
        if not connection_successful:
            print("Connexion fermée en raison d'une réponse incorrecte.")

if __name__ == "__main__":
    main()