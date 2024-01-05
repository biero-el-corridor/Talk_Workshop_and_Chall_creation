<img src="picture/muscle_brute.png" align="center" width=40% height=40%>

## Contexte technique. 
le challenge se compose de 5 docker 

4 docker pour la partie investigation 
- 1 docker pour la partie graphique et le back de Arkime 
- 3 docker pour OpenSearch

1 docker pour répondre au questions

tout se qui et lier a chalenge en luis méme et dans 
## Setup de l'environement. 

### Setup de l'environement [Arkime](https://arkime.com/)

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

# run the script that will parse and upload 
docker exec -it [container-id] ./data/arkime-parse-pcap-folder.sh

# manque le flag de compilations pour push sorrectemtn le pcap. 

```

### Setup docker questions réponse

```sh 

docker run -d -p 56789:56789 --name Q_and_A_docker python

docker cp /socket_open_Q_and_A.py docker_name:/home 

docker exec docker_id python /home/socket_open_Q_and_A.py

nc docker_IP 56789
```