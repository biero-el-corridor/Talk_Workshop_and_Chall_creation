
### $Nuclei$  $:$ $from$ $user$ $to$ $writer$

Nuclei c'est le mec rigolo dans la cours de récrée , qui en secret vole toute ces blague a un humouriste qui s'appelle nmap. 

---
<grid drop="-25 0"  drag="100 0" align="topleft"  >
C'est quoi Nuclei ? 
</grid>

![[pic_nuclei/image-11.png|800]]

<grid drag="100 6" drop="bottom">
###### © 2025 biero-el-corridor beeroverflow<!-- element style="font-weight:300" -->
</grid>
---
<grid drop="-25 0"  drag="100 0" align="topleft"  >

Vous avez dit template ? (1/2) 
</grid>

```yaml
id: loytec-default-password

info:
  name: Loytec PLC - Default Login
  author: biero-el-corridor
  severity: high
  description: |
    Identified Loytec PLC web interfaces that were accessible using default credentials (admin:loytec4u). These devices were commonly deployed in building automation and industrial control environments. When left unchanged, default credentials could have allowed unauthorized users to gain administrative access to the system.
  metadata:
    verifed: true
    max-request: 1
  tags: loytec,default-login

variables:
  username: admin
  password: loytec4u
```

<grid drag="100 6" drop="bottom">
###### © 2025 biero-el-corridor beeroverflow<!-- element style="font-weight:300" -->
</grid>
---
<grid drop="-25 0"  drag="100 0" align="topleft"  >
Vous avez dit template ? (2/2) 

</grid>

```yaml
http:
  - raw:
      - |
        POST /webui/login HTTP/1.1
        Host: {{Hostname}}
        X-Create-Session: 1
        Content-Type: application/x-www-form-urlencoded
        username={{username}}&password={{password}}&login=Login
    
    matchers-condition: and
    matchers:
      - type: word
        part: body
        words:
          - '"sessUser":"admin"'
          - '"loggedIn":true'
        condition: and  
      - type: status
        status:
          - 200
```

<grid drag="100 6" drop="bottom">
###### © 2025 biero-el-corridor beeroverflow<!-- element style="font-weight:300" -->
</grid>
---
Network fingerprinting , le copilote de nuclei.

---
<grid drop="-25 0"  drag="100 0" align="topleft"  >

Network fingerprinting , le copilote de nuclei. 
</grid>

![[pic_nuclei/Network Fingerprint.png]]

<grid drag="100 6" drop="bottom">
###### © 2025 biero-el-corridor beeroverflow<!-- element style="font-weight:300" -->
</grid>

---

![[pic_nuclei/image-17.png]]

---

<grid drop="-25 0"  drag="100 0" align="topleft"  >

Supply Chain de la conpot (1/6). 
</grid>

![[pic_nuclei/image-14.png|1800]]

<grid drag="100 6" drop="bottom">
###### © 2025 biero-el-corridor beeroverflow<!-- element style="font-weight:300" -->
</grid>

---
<grid drop="-25 0"  drag="100 0" align="topleft"  >

Supply Chain de la conpot (2/6). 
</grid>

![[pic_nuclei/image(1).png]]

<grid drag="100 6" drop="bottom">
###### © 2025 biero-el-corridor beeroverflow<!-- element style="font-weight:300" -->
</grid>
---
<grid drop="-25 0"  drag="100 0" align="topleft"  >

supply chain de la conpot (3/6). 
</grid>

![[image-16.png]]

<grid drag="100 6" drop="bottom">
###### © 2025 biero-el-corridor beeroverflow<!-- element style="font-weight:300" -->
</grid>
---
<grid drop="-25 0"  drag="100 0" align="topleft"  >
Supply Chain de la conpot (4/6). 
</grid>

![[pic_nuclei/image.png]]

<grid drag="100 6" drop="bottom">
###### © 2025 biero-el-corridor beeroverflow<!-- element style="font-weight:300" -->
</grid>
---
<grid drop="-25 0"  drag="100 0" align="topleft"  >

Supply Chain de la conpot (5/7). 
</grid>

![[pic_nuclei/image-13.png]]

<grid drag="100 6" drop="bottom">
###### © 2025 biero-el-corridor beeroverflow<!-- element style="font-weight:300" -->
</grid>


---
<grid drop="-25 0"  drag="100 0" align="topleft"  >

Supply Chain de la conpot (6/7). 
</grid>

![[pic_nuclei/image-7.png]]

<grid drag="100 6" drop="bottom">
###### © 2025 biero-el-corridor beeroverflow<!-- element style="font-weight:300" -->
</grid>

---
<grid drop="-25 0"  drag="100 0" align="topleft"  >

Supply Chain de la conpot (7/7). 
</grid>

![[pic_nuclei/image-15.png|401x190]]

<grid drag="100 6" drop="bottom">
###### © 2025 biero-el-corridor beeroverflow<!-- element style="font-weight:300" -->
</grid>
---
<grid drop="-25 0"  drag="100 0" align="topleft"  >
Conclusions
</grid>


<font size=6>
<grid drop="-2 10"  drag="120 20" align="top" style="text-align:left" >

- Si vous voulez faire des PoC rapide sur des attaque web ou sur la couche réseaux nuclei et super utile.

- ll ne se contente pas que de faire de l'html.

- Si sa vous intéresse une vague te Template tcp sur système CPS devrais arriver.

- https://github.com/biero-el-corridor/Talk_Workshop_and_Chall_creation/tree/main/Talk

</grid>
</font>
