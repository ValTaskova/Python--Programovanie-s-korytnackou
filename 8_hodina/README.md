# 8. hodina

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

Ďalej sme generovali náhodné čísla. Na to sme useli použiť funkciu *randint* z knižnice *random*, ktorú bolo potrebné importovať. Výsledok funkcie sme ukladali do premennej.

```python
import turtle
from random import randint

dlzka = randint(50,100)                       #generovanie nahodneho cisla
write(dlzka, font=("Arial", 30, "italic"))    #vypísanie hodnoty premennej dlzka

goto(randint(-500,500), randint(-500,500))    #korytnacka ide na nahodnu poziciu
```

Nakoniec sme si ukázali podmienky. Tie slúžia na rozvetvenie programu. pokial je podmienka pravdivá, tak sa vykoná kód vo vnútri podmienky.

```python
if dlzka < 60:    #pokial je cislo v premennej dlzka mensie ako 60, tak sa vykona nasledujuci riadok
    dlzka = 60    #nastavi dlzku na hodnotu 60
```

**Príkazy z minulej hodiny:**
| if ... :  | Ak ... | Ak je ... pravda, tak vykonaj to čo následuje |

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
| randint(...,...)  | Náhodné prirodzené číslo  | Vygeneruje náhodné číslo v rozmedzií od ... po ... |


*Tri bodky v zátvorkách znamenajú, že treba niečo doplniť.*
