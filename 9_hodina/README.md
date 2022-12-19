# 9. hodina

Na hodine sme pokračovali s podmienkami. Nemusíme zakaždým písať nové *if* aj pokiaľ sa to týka tej istej veci ako napr. testujeme či je číslo menšie než nejaká hodnota, ak
nie, tak či je z nejakého intervalu/rozmedzia číslel alebo chceme pokryť všetky ostatné prípady. K tomu nám pomáhaju ďalšie podmienky *elif* a *else*, avšak viažú sa k
predchádzajúcemi *if*, ktoré musí existovať. 

```python
if (loteria <= 5):                        #ak je premenna loteria mensia alebo rovna 5
    write("Nevyhral si") 
elif (loteria > 5 and loteria <= 20):     #alebo ak je premenna loteria vacsia ako 5 A ZAROVEN mensia alebo rovna 20
    write("Ciastocna vyhra")
elif (loteria > 20 and loteria <= 29):    #alebo ak je premenna loteria vacsia ako 20 A ZAROVEN mensia alebo rovna 29
    write("Vacsinova vyhra")
else :                                    #inak
    write("Kompletna vyhra")
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
| randint(...,...)  | Náhodné prirodzené číslo  | Vygeneruje náhodné číslo v rozmedzií od ... po ... |
| if ... :  | Ak ... | Ak je ... pravda, tak vykonaj to čo následuje |
| else :  | Inak ... | Inak vykonaj to čo následuje |
| elif ... :  | Inak ak ... | Alebo ak je ... pravda, tak vykonaj to čo následuje |

*Tri bodky v zátvorkách znamenajú, že treba niečo doplniť.*
