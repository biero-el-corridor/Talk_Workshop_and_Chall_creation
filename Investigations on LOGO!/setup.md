

## Arkime setup. 

https://hub.docker.com/r/mammo0/docker-arkime


```sh

# pull the docker 
docker pull mammo0/docker-arkime
# git clone the repos
git clone https://github.com/mammo0/docker-arkime
cd docker-arkime
# change the .env docker name to be compliant with the install
mv docker-compose.env .env

#############################################
# apply the OpenSearch recomendations 
#############################################
sudo swapoff -a
# add a value 
echo "vm.max_map_count=262144" >> /etc/sysctl.conf
sudo sysctl -p
# verify that you have wite to the file with a tial command
#############################################
#############################################

# run the docker compose 
docker-compose up -d

# wait a little bit 

## edit the commande to move the pcap directly to the docker 

docker cp /path/to/the/pcap/folder/ docker-arkime_arkime_1:/data/pcap

##### on the docker 
# import the pcap file. 
/opt/arkime/bin/capture --copy -n * -R /folder/where/you/cp/the/pcap/folder

```


### Challenge questions responce docker 


docker pulll python on port 56789:56789


le script a appliquer 

```python
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
        print(f"Connexion établie avec {addr}")

        # Updated questions and answers
        questions = ["Quelle est l'IP de la machine?", "Quel est le port par lequel la personne est passée?"]
        answers = ["10.1.1.1", "22"]

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
```