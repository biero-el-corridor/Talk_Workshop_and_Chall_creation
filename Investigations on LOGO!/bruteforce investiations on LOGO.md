

## histoire 

on c'est fait avoir un attaquant a réussi a rentrer dans nos systéme et a fait en sorte de se faire voire via une  TTP particuliérement bruiante , mais il a étée assez rapide pour mettre a mal un PLC qui controlais des arrivée d'air sous pressions avent qu'on intervienne , une cuve a étée détruite et une autre a été endommagée, nous avions des TAP réseaux on a réussi a remonter les minute critique  sur notre ARKIME.

C'est a vous de jouer , répondez au questions de votre chef. 
## concept 

mettre en place un arkime avec une journée de pcap sur le lab 

le chall se passe sous la forme d'une investigations 

l'objectif et de trouver les chose suivante.
## structure 

chall level: medium
catégorie: network investigations , ICS.
## question
- quelle et l'ip de la machine qui se fait attaquer.
- quelle et le nom du produit qui se fait attaquer. 
- l'attaquant a taper directement le point sensible , il a du faire une phase de reconnaissance ,
	- quelle serait l'outils qu'il a utiliser pour effectuer la reconnaissance sur le PLC ? 
		- nmap. 
	- avec cette outils , quelle sont les emplacment mémoire qu'il a "scanner"
		- snap7. 
	- quelle emplacement mémoire va t'il scanner au moin 3 fois ? 
		- 1064.0,1064.1,1064.2,1064.3,1064.4,1064.5
	- on peut constater que quelle emplacement mémoire a le plus bouger ? 
		- 1064.2,
- la pahse de reconaissence et finie , l'attaquant passe a la suite 
- quelle et le code mitre du TTP de la seconde partie de l'attaque ? 
	- ([T1110](https://attack.mitre.org/techniques/T1110/)). 
- quelle et le 14éme "Security hint".
	- du a la strucutre de la rest api c'est le crc32  du xor du chall  + le mdp qui et afficher , mais en copian le hint en spoofant l'ip celas peut marcher.  
- quelle et le security hint qui marche ?  
	- voir reste. 
- quelle et la versions du firmware.  
	- voir dans le retours web. 
- quelle valeur sont modifier via l'interface web ? 
	- voir les SETVAR dans le follow tcp stream
- quelle sont les status finaux des coil quand la déconnexions de la sessions qu'on investigue ?
	- 1,1,1
- combien de temps (arrondie a la moitié de minute) a durée l'attaque (entre le début du nmap et la déconnexions de l'attaquant)


## a faire

- [ ] nmap -sS (TCP SYN scan) 
![[1632325814859.png]]

- [ ] laught read functions on port 102 
- [ ] remake the attaque on a 5 minute range 
- [ ] wait 5 min 
- [ ] laught bruteforce attack again web base logo 
- [ ] mofify value multiple time 
- [ ] let the conf at the end a 1,1,1
- [x] create the docker and the questions via nc 
	- [ ] apply all the awnsser and the responce. 