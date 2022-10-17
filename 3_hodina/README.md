# 3. hodina

Na hodine sme sa zoznámili so súradnicami a ako pomocou nich vieme popísať priestor. Na obrázku vidíme, ako vyzerá súradnicová sústava pre Python korytnačku. Pomocou čísel
na priamke X (šírka) a Y (výška) si vieme určiť, kde sa daný bod nachádza. Je zaužívané, že najskôr hovoríme súradnicu X (šírku) a potom súradnicu Y (výšku). 

<img src="https://user-images.githubusercontent.com/93611731/196229081-8bde5db1-a115-4c60-b8a4-1dddc4f9cb5c.jpg" height="450" width="500" >


Súradnice bodov vieme určiť ako:
| Bod  | X | Y |
| ------------- | ------------- | ------------- |
| červený  | 200  | 200 |
| čierny  | 300  | 100 |
| zelený  | 300  | -100 |
| modrý  | -100  | -200 |


## Príkazy
Naučili sme sa nové príkazy, *pos()* a *goto()*. Príkaz *pos()* nám zistí pozíciu korytnačky. Pokiaľ ju chceme zobraziť, potrebujeme ho vypísať pomocou príkazu *write()*, 
ktorý sme sa naučili na minulej hodine. Príkaz *goto(X, Y)* nám premiestni korytnačku na zvolenú pozíciu.
```python
goto(300, 100)  #premiestni korytnačku na súradnice X=300 a Y=100, teda tam, ako je cierny bod na obrazku
```

**Príkazy z dnešnej hodiny:**
| Príkaz  | Preklad | Čo to znamená |
| ------------- | ------------- | ------------- |
| pos()  | Pozícia, poloha, súradnice | Získa súradnice korytnačky |
| goto(*X*, *Y*)  | Choď na  | Presunie korytnačku na dané súradnice |

**Príkazy z minulej hodiny:**
| Príkaz  | Preklad | Čo to znamená |
| ------------- | ------------- | ------------- |
| from turtle import *  | Z korytnačky načítaj *  | Načítaj všetky funkcie z knižnice Korytnačka |
| showturtle()  | Ukáž korytnačku  | Zobrazí korytnačku |
| done()  | Spravené, hotovo  | Skončí program |
| forward(...)  | Dopredu  | Posunie korytnačku dopredu |
| left(...)  | Doľava  | Otočí korytnačku doľava |
| right(...)  | Doprava  | Otočí korytnačku doprava |
| delay(...)  | Meškanie, oneskorenie  | Spomalí program (1 sekunda = 1000) |
| penup()  | Pero hore  | Vypne kreslenie |
| pendown()  | Pero dole  | Zapne kreslenie |
| pencolor(‘...‘)  | Farba pera  | Zmení farbu pera |
| write(“…”)  | Napíš  |	Napíše text tam, kde sa nachádza korytnačka |
| pensize(...)  | Hrúbka pera  | Nastaví hrúbku pera |
| bgcolor(‘...‘)  | Farba pozadia  | Zmení farbu pozadia |

*Tri bodky v zátvorkách znamenajú, že treba niečo doplniť.*

