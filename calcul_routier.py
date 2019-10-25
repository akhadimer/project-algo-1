from math import *
from time import *

villes_existantes = ['marseille', 'toulouse', 'paris', 'perpignan']
villes_distances = [['marseille',['toulouse',403],['paris',773],['perpignan',317]],
                    ['toulouse',['marseille',403],['paris',676],['perpignan',207]],
                    ['paris',['marseille',773],['toulouse',676],['perpignan',846]],
                    ['perpignan',['marseille',317],['toulouse',207],['paris',846]],]

def calcul_routier(ville_depart,ville_arrivee):
    for pos in range(len(villes_distances)):
        if ville_depart == villes_distances[pos][0]:
            case_ville_dep = pos
            break
    for pos in range(len(villes_distances)):   
        if ville_arrivee == villes_distances[case_ville_dep][pos][0]:
            distance = villes_distances[case_ville_dep][pos][1]
            break
    
    e = distance/84
    if (e%1 == 1):
        r = (e * 3600) + ((e/2) * 900)
    else:
        e2 = floor(e) - 1
        t1 = (e2 * 3600) + (e2 * 900)
        j = distance - (e2 * 84)
        f = j - 7.5
        t2 = ((f * 100)/25)
        r = t1 + t2 + 540
        r = strftime('%H %M', gmtime(r))
        
    return ([ville_depart,ville_arrivee,distance, r])

"""
ville_depart_exist = False
ville_arrivee_exist = False
print ("Villes disponibles pour le départ et l'arrivée du camion : Marseille, Toulouse, Paris, Perpignan")
while True:
    ville_depart = input('Entrez la ville de départ : ').lower()
    for position in range(len(villes_existantes)):
        if villes_existantes[position] == ville_depart:
            ville_depart_exist = True
            break
        if position == len(villes_existantes) - 1:
            print ('La ville n\'existe pas !') 
    if ville_depart_exist == True:
        break

while True:
    ville_arrivee = input('Entrez la ville d\'arrivee : ').lower()
    for position in range(len(villes_existantes)):
        if ville_depart == ville_arrivee:
            print ('Vous ne pouvez pas choisir la même ville que celle de départ !')
            break
        if villes_existantes[position] == ville_arrivee:
            ville_arrivee_exist = True
            break
        if position == len(villes_existantes) - 1:
            print ('La ville n\'existe pas !') 
    if ville_arrivee_exist == True:
        break
"""
tab = calcul_routier('marseille','toulouse')

print (tab)