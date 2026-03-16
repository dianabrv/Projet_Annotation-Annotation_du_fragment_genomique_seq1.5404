#!/bin/env python

import sys

if len(sys.argv) < 4 : 
    print("Bienvenue sur convertisseur_sfm_GFF. Pour utiliser le programme, veuillez saisir votre fichier de résultats scan_for_matches suivis du type de recherche : RBS, promoteur, terminateur ou le nom d'un motif autre que vous avez chercher. Terminez par saisir le nom du fichier de sortie.")
    sys.exit(1)

fichier=sys.argv[1] #récupération des trois entrées 
f_sortie=sys.argv[3]

with open(fichier, "r") as fichier_entree, open(f_sortie, "w") as fich_sortie : # ouverture du fichier d'entrée et de sortie
    for ligne in fichier_entree : # découpage des lignes et suppression des espaces
        ligne=ligne.strip()  # on enlève les espaces
        if ligne.startswith(">"): # si la ligne commence comme ça on aura les positions du motifs
            ligne=ligne.replace(">","").replace("[","").replace("]","").replace(":",",") # nettoyage           
            colonnes=ligne.split(",") # séparation par les virgules
            nom_seq=colonnes[0] # récupération du nom de la seq
            debut=int(colonnes[1])
            fin=int(colonnes[2])
            if debut < fin :
                strand="+"
            else : 
                strand="-"                
        else :
            ligne.replace("", ",")
            colonnes=ligne.split(",")        
            sortie=f'{nom_seq}\tscan_for_matches\t{sys.argv[2]}\t{debut}\t{fin}\t.\t{strand}\t.\tnote "{colonnes[0]}"\n'
            fich_sortie.write(sortie)
            if strand == "+" and sys.argv[2]=="RBS" : # formatage de l'ATG
                sortie=f"{nom_seq}\tscan_for_matches\tATG\t{fin-2}\t{fin}\t.\t{strand}\t.\n"
                fich_sortie.write(sortie)
            elif sys.argv[2]=='RBS' :
                sortie=f"{nom_seq}\tscan_for_matches\tATG\t{fin+2}\t{fin}\t.\t{strand}\t.\n"                
                fich_sortie.write(sortie)
