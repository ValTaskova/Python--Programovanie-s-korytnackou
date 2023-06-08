# 7. hodina

Na hodine sme pokračovali s funkciami, ukázali sme si použitie náhodných čísel a podmienok. Pokiaľ chceme meniť hodnotu vo funkcií, napr. počet krokov, ktoré má korytnačka
prejsť, tak musíme tam tú hodnotu (počet krorkov) poslať pomocou premennej alebo čísla. 
```python
def stvorec(strana):            #definicia funkcie -> nazov + zatvorky, kde je nasa premenna, ktoru tam posielame
    penup()
    forward(200)
    pendown()
    for i in range(4):
        forward(strana)
        right(90)

strana = 100
stvorec(strana)                 #volanie funkcie pomocou premennej
stvorec(100)                    #volanie funkcie pomocou cisla
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
