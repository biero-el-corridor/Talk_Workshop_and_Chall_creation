

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

