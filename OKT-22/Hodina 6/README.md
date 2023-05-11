# 6. hodina

Na hodine sme sa zoznámili s cyklom *for*. Pomocou neho vieme opakovať riadky kódu bez toho, aby sme ich museli písať ručne pod sebou niekoľkokrát.

**Bez cyklu**
```python
dlzka = 5
forward(dlzka)
right(90)

dlzka = dlzka + 5
forward(dlzka)
right(90)

dlzka = dlzka + 5
forward(dlzka)
right(90)

dlzka = dlzka + 5
forward(dlzka)
right(90)
```

**S cyklom**
```python
dlzka = 5

for i in range(4)
  forward(dlzka)
  right(90)
  dlzka = dlzka + 5
```


**Príkazy z dnešnej hodiny:**
| Príkaz  | Preklad | Čo to znamená |
| ------------- | ------------- | ------------- |
| for i in range(...):  | Pre i v rozmedzí ...  | Opakuj ...-krát |

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

*Tri bodky v zátvorkách znamenajú, že treba niečo doplniť.*
