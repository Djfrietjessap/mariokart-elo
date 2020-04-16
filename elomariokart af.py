
import math
def kans (dic_elo,naam1,naam2): # functie die de kansen berekent
    kans1 = 1 / (1 + 10**((dic_elo.get(naam2,"")- dic_elo.get(naam1,""))/400)) # formule elo kans
    kans2 = 1 / (1 + 10**((dic_elo.get(naam1,"") - dic_elo.get(naam2,""))/400))
    return (kans1,kans2,"De kans dat " + naam1 + " wint is " + str(kans1* 100) + "%" +", de kans dat " + naam2 +" wint is " + str(kans2* 100) + "%" )



def slokken(dic_elo,naam1,naam2): # functie die berekent hoeveel slokken dat je moet drinken als je veliest
    slokken_coefficient = 6
    kans1 = kans(dic_elo,naam1,naam2)[0]
    kans2 = kans(dic_elo, naam1, naam2)[1]
    aantal_slokken_naam1 = math.ceil(kans1 * slokken_coefficient) # zelf gemaakte formule die werkt met kans gewichten
    aantal_slokken_naam2 = math.ceil(kans2 * slokken_coefficient)
    return("Als " + naam1 + " verliest moet hij " + str(aantal_slokken_naam1) + " slokken drinken," + "Als " + naam2 + " verliest moet hij " + str(aantal_slokken_naam2) + " slokken drinken")




def nieuwe_elo(dic_elo,naam1,naam2,winnaar): #functie die de nieuwe elos bepaalt

    k_coeficient = 30
    verwachting1 = kans (dic_elo,naam1,naam2)[0] #verwacthing komt overeen met de kans
    verwachting2 = kans(dic_elo, naam1, naam2)[1]
    if winnaar == naam1:
        uitkomst1 = 1 #dit is de uitkomst van het spel (wie er wint dus krijgt 1 de andere 0)
        uitkomst2 = 0

    elif winnaar == naam2:
        uitkomst1 = 0
        uitkomst2 = 1
    nieuwe_elo_naam1 =  dic_elo.get(naam1,"") + k_coeficient *(uitkomst1 - verwachting1) #formule nieuwe elo
    nieuwe_elo_naam2 =  dic_elo.get(naam2,"") + k_coeficient *(uitkomst2 - verwachting2)
    return (nieuwe_elo_naam1, nieuwe_elo_naam2, "De nieuwe elo voor "+ naam1 + " is " + str(nieuwe_elo_naam1)+","+"De nieuwe elo voor "+ naam2 + " is " + str(nieuwe_elo_naam2) )


def print_functie_voor_spel(dic_elo, naam1, naam2): #dit print al de gegevens voor het spel

    print(kans(dic_elo, naam1, naam2)[2])
    print(slokken(dic_elo, naam1, naam2))


def print_functie_na_spel(dic_elo, naam1, naam2,winnaar):
    print(nieuwe_elo(dic_elo, naam1, naam2,winnaar)[2])

def app():
    dic_elo = {"Tobias": 1500, "Simon": 1800, "Sam": 1500}
    while True:
         print("wie vs wie?")
         naam1 = str(input())
         naam2 = str(input())
         print_functie_voor_spel(dic_elo, naam1, naam2)
         print("Wie heeft er gewonnen?")
         winnaar = str(input())
         print_functie_na_spel(dic_elo, naam1, naam2, winnaar)
         dic_elo[naam1] = nieuwe_elo(dic_elo, naam1, naam2,winnaar)[0]
         dic_elo[naam2] = nieuwe_elo(dic_elo, naam1, naam2,winnaar)[1]
app()