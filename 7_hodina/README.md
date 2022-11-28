# 7. hodina

Na hodine sme pokračovali s cyklami. Ukázali sme si vnorené cykly, teda cyklus, ktorý sa nachádza v inom cykle a to tak, že sme kreslili štvorec vedľa seba. Najskôr sme sa 
museli posunúť a potom sme vykreslili štvorec. Ukázali sme si, čo by sa stalo, keby cykly prehodíme, teda najskôr by sme chceli vykresliť štvorec v prvom cykle a posunúť sa 
vo vnorenemom cykle. Nakoniec sme si ukázali, že z akéhokoľvek kódu vieme spraviť vlastnú funkciu, ktorú si vieme zavolať. 

```python
def stvorec():            #definicia funkcie -> nazov + zatvorky
    penup()
    forward(200)
    pendown()
    for i in range(4):
        forward(dlzka)
        right(90)
              
stvorec()                 #volanie funkcie
```

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
| pos()  | Pozícia, poloha, súradnice | Získa súradnice korytnačky |
| goto(*X*, *Y*)  | Choď na  | Presunie korytnačku na dané súradnice |
| for i in range(...):  | Pre i v rozmedzí ...  | Opakuj ...-krát |

*Tri bodky v zátvorkách znamenajú, že treba niečo doplniť.*
