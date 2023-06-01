# 4. hodina

Na hodinách sme sa zoznámili s premennými a s tým, ako ich používať. Premenné slúžia na to, aby nám uložili nejaké číslo, s ktorým chceme pracovať. Pokiaľ kreslíme
štvorec, veľkosť strany si uložime do premennej, ktorú môžeme ďalej používať. Výhodou je, že pokiaľ veľkosť strany chceme zmeniť, stačí zmeniť len jedno číslo.

```python
strana1 = 300           #premenna strana1 ma hodnotu 300

forward(strana1)
left(uholStvorca)
forward(strana1)
left(uholStvorca)
forward(strana1)
left(uholStvorca)
forward(strana1)
left(uholStvorca)
```
S premennými vieme robiť aj matematické príklady, ako sčitanie, odčítanie, násobenie, delenie, modulo. Modulo (%) nám dá zvyšok po delení, teda napr. 7 / 5 = 1 zvyšok 2, teda
7 % 5 = 2.

```python
strana1 = 300 * 2          #premenna strana1 ma hodnotu 300 * 2, teda 600
strana2 = strana1 + 100    #premenna strana2 ma hodnotu 600 + 100, teda 700
strana3 = 300 / 2          #premenna strana3 ma hodnotu 300 / 2, teda, 150

strana1 = 300              #premenna strana1 ma hodnotu 300 a v dalsich prikazoch sa bude pouzivat tato hodnota
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

*Tri bodky v zátvorkách znamenajú, že treba niečo doplniť.*
