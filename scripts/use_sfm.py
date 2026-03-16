#!/bin/env python

import sys
import subprocess

if len(sys.argv) < 4 : 
    print("Bienvenue sur use_sfm. Pour utiliser le programme, veuillez saisir votre séquence suivis du nom du fichier de sortie et enfin une des trois options disponibles pour B.subtilis : RBS, promoteur ou terminateur. Pour une recherche spécifique, donnez en troisième le fichier contenant le pattern à chercher.")
    sys.exit(1)

seq=sys.argv[1] #récupération des trois entrées 
sortie=sys.argv[2]
query=sys.argv[3]

if query=="RBS" : # si on cherche RBS
    motifs=["rbs1.txt", "rbs2.txt"] # on vas tester 2 motifs différents
    with open(seq, "r") as fich_entree, open(sortie, "w") as fich_sortie: # ouverture de la sequence en format fichier et sortie en format écriture
        for motif in motifs : # on test chaque motifs
            fich_entree.seek(0) # se remettre au début du fichier à parcourrir
            commande=["./scan_for_matches", "-c", motif] # execution de scan for matches 
            subprocess.run(commande, stdin=fich_entree, stdout=fich_sortie)             
    print("Voici un aperçu des résultats qui sont stocker dans", sortie, "pour la recherche :", query)
    subprocess.run(["head", sortie])

elif query=="promoteur" :
    commande=["./scan_for_matches", "-c", "promoteur.txt"] # execution de scan for matches
    with open(seq, "r") as fich_entree, open(sortie, "w") as fich_sortie: # ouverture de la sequence en format fichier et sortie en format écriture
            subprocess.run(commande, stdin=fich_entree, stdout=fich_sortie)             
    print("Voici un aperçu des résultats qui sont stocker dans", sortie, "pour la recherche :", query)
    subprocess.run(["head", sortie])

elif query=="terminateur" :
    commande=["./scan_for_matches", "-c", "terminateur.txt"] # execution de scan for matches
    with open(seq, "r") as fich_entree, open(sortie, "w") as fich_sortie: # ouverture de la sequence en format fichier et sortie en format écriture
            subprocess.run(commande, stdin=fich_entree, stdout=fich_sortie)             
    print("Voici un aperçu des résultats qui sont stocker dans", sortie, "pour la recherche :", query)
    subprocess.run(["head", sortie])

else : 
    commande=["./scan_for_matches", "-c", query] # utilisation de scan for matches personnalisée
    with open(seq, "r") as fich_entree, open(sortie, "w") as fich_sortie: # ouverture de la sequence en format fichier et sortie en format écriture
            subprocess.run(commande, stdin=fich_entree, stdout=fich_sortie)             
    print("Voici un aperçu des résultats qui sont stocker dans", sortie, "pour la recherche personnalisée")
    subprocess.run(["head", sortie])