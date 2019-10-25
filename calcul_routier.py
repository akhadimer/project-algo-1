villes_existantes = ['marseille', 'toulouse', 'paris', 'perpignan']
villes_distances = [['marseille',['toulouse',403],['paris',773],['perpignan',317]],
                    ['toulouse',['marseille',403],['paris',676],['perpignan',207]],
                    ['paris',['marseille',773],['toulouse',676],['perpignan',846]],
                    ['perpignan',['marseille',317],['toulouse',207],['paris',846]],]

def calcul_routier(ville_depart,ville_arrivee):
    vitesse = 0
    temps_minutes = 0
    distance_parcourue = 0
    for pos in range(len(villes_distances)):
        if ville_depart == villes_distances[pos][0]:
            case_ville_dep = pos
            break
    for pos in range(len(villes_distances)):   
        if ville_arrivee == villes_distances[case_ville_dep][pos][0]:
            distance = villes_distances[case_ville_dep][pos][1]
            break
    
    while (distance_parcourue < distance):
        if vitesse == 90:
            temps_minutes += 1
        if vitesse < 90:
            vitesse += 10
            temps_minutes += 1
        distance_parcourue = distance_parcourue + vitesse / 60

    return ([ville_depart,ville_arrivee,distance, temps_minutes])

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