import socket

def handle_connection(client_socket, question, correct_answer):
    client_socket.sendall(question.encode())
    response = client_socket.recv(1024).decode()
    
    if response.lower().strip() == correct_answer.lower().strip():
        client_socket.sendall("Good answer!\n".encode())
        return True
    else:
        client_socket.sendall("Incorrect answer. The connection is terminated.\n".encode())
        return False

def main():
    host = '0.0.0.0'
    port = 56789  # Port is modified to 56789

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Waiting for connections on the port {port}...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection established with {addr} the elements between () are the flag format x corresponds to a lower case letter X corresponds to an upper case letter. The size of the sample format does not always correspond to the size of the flag, there are about fifteen questions.")

        # Updated questions and answers
        questions = ["What tools would he use to carry out the network recognitions phase ? And with which flag (xxxxx -xxx)?",
        "What seen to be the IP of the victim ?",
        "Which and the name of the product being attacked (manufacturer and product name, in lower case (xxxx xxxxx)).",
        "Ok, so it scanned with nmap, but it must have tried to request the siemens PLC with another tool on the s7comm protocol. What was that tool?",
        "Which memory location will it scan at least 3 times (XXXX.X,XXXX.X)?",
        "the recognition stage is over, the attacker moves on to the next stage (press Enter)."
        "What is the TTP MITRE code for the second part of the attack? (TXXX)",
        "What are the \"Security hint \" from the attacker's 1st bruteforce attempt",
        "Which security hint works?",
        "What is the LOGO! Firmware version (X.XX.XX = veritable lenght)?", 
        "one of the features of the web interface is the ability to add I/O to modify its content. Which I/O have been added? (XX,XX,XX)",
        "Has it removed one of the I/Os, and if so, which one (XX,XX)?",
        "What is the final status of the coil when it is disconnected from the session being investigated ?(X.X.X.X.X.X)", 
        "What is the MITRE ATT&CK ICS code corresponding to the attacker's actions (TXXXX)?", 
        "how long (rounded to the tenth superior) did the attack last (between the start of the nmap and the attacker's disconnections) (X:XX)",
        "GG weel played , contact biero on discord, il te donneras le flag"]
        
        answers = ["nmap -sS", "10.1.1.15","siemens logo!","snap7","1064.0,1064.1,1064.2,1064.3,1064.4","T1110","AE727A62B0813B2ADB37B83B50DD5D25","9E2D4B28BDCCE7C1BACFC0E7E51C55F7","1.83.02","1.1.1.0.0","Q1,Q2,Q3,Q4","Q4","1.1.1","T0806","5:30"]

        connection_successful = True

        for i, question in enumerate(questions):
            if not handle_connection(client_socket, f"Question {i+1}: {question}\Anwser: ", answers[i]):
                connection_successful = False
                break
        client_socket.close()
        if not connection_successful:
            print("Connection closed due to incorrect response.")

if __name__ == "__main__":
    main()