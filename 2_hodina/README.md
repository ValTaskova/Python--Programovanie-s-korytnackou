# 2. hodina

Na hodine sme si zopakovali príkazy, ktoré nám zobrazili korytnačku, posúvali ju, otáčali ju alebo ju spomalili. Ďalej sme si ukázali nové príkazy, ktoré nám upravili
farbu alebo hrúbku čiary, farbu pozadia, napísalo text a zapli alebo vypli pero. Taktiež sme si hľadali farby na internete, pričom na stránke https://trinket.io/docs/colors
si vieme ľahko zistiť názov farby tým, že na ňu klikneme a skopírujeme jej názov, teda *Turtle name*.

Príkazy z minulej hodiny:
| Príkaz  | Preklad | Čo to znamená |
| ------------- | ------------- | ------------- |
| from turtle import *  | Z korytnačky načítaj *  | Načítaj všetky funkcie z knižnice Korytnačka |
| showturtle()  | Ukáž korytnačku  | Zobrazí korytnačku |
| done()  | Spravené, hotovo  | Skončí program |
| forward(...)  | Dopredu  | Posunie korytnačku dopredu |
| left(...)  | Doľava  | Otočí korytnačku doľava |
| right(...)  | Doprava  | Otočí korytnačku doprava |
| delay(...)  | Meškanie, oneskorenie  | Spomalí program (1 sekunda = 1000) |

Príkazy z dnešnej hodiny:
| Príkaz  | Preklad | Čo to znamená |
| ------------- | ------------- | ------------- |
| penup()  | Pero hore  | Vypne kreslenie |
| pendown()  | Pero dole  | Zapne kreslenie |
| pencolor(‘...‘)  | Farba pera  | Zmení farbu pera |
| write(“…”)  | Napíš  |	Napíše text tam, kde sa nachádza korytnačka |
| pensize(...)  | Hrúbka pera  | Nastaví hrúbku pera |
| bgcolor(‘...‘)  | Farba pozadia  | Zmení farbu pozadia |

*Tri bodky v zátvorkách znamenajú, že treba niečo doplniť*

Príkaz *write* sme rozšírili, aby sme mohli zmeniť veľkosť písma, pričom vieme tiež nastaviť aj typ a štýl písma.
```python
write("CIARA \"?\" ", font=("Arial", 30, "italic"))   #pismo moze byt normal, bold, italic
```

Tiež sme si ukázali ako vyplniť nejaký útvar farbou:
```python
fillcolor('yellow')     #Vyplni utvar farbou
begin_fill()            #Zacina sledovat co ma vyplnit

left(90)                #Nas utvar - trojuholnik
forward(100)
left(120)
forward(100)
left(120)
forward(100)

end_fill()              #Prestane sledovat a vyplni utvar farbou 

```
