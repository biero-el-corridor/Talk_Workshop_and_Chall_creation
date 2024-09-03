<img src="picture/muscle_brute.png" align="center" width=40% height=40%>

## story

An attacker managed to get into our system and was able to make himself seen via a particularly noisy TTP, but he was quick enough to damage a PLC which controlled the arrival of pressurized air. By the time we intervened, one tank had been destroyed and another had been damaged. We had network TAPs, and we managed to get the critical minutes back on our ARKIME.
It's up to you to answer your boss's questions.
here's a quick network diagram to help you understand the network environment

## concept
Set up an Arkime with a day of pcap on the lab
The chall takes the form of an investigation
The objective is to find the following. Structure

### Chall level:
- medium

### category:
- network investigations.
- SIEM Investigations.
- ICS.

### Technical context.

The challenge consists of 5 dockers:
- 4 dockers for the investigation part
- 1 docker for the graphics and back end of Arkim
- 3 docker for OpenSearch. 

- 1 docker for answering the questions.

Everything linked to solve the challenge itself are in the Q&A docker, you need to install it , read the instructions at the end of this README.

## Setup of the environement. 

### Setup of [Arkime](https://arkime.com/) environment

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
/opt/arkime/bin/capture --copy -n 4 -r /folder/where/you/cp/the/pcap/file.pcapng

# run the script that will parse and upload 
docker exec -it [container-id] ./data/arkime-parse-pcap-folder.sh

# manque le flag de compilations pour push sorrectemtn le pcap. 

```

### Setup docker Q&A

```sh 

docker run -d -p 56789:56789 --name Q_and_A_docker python

docker cp /socket_open_Q_and_A.py docker_name:/home 

docker exec docker_id python /home/socket_open_Q_and_A.py

nc docker_IP 56789
```