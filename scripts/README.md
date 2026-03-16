# Scripts et Automatisation
Cette section regroupe les outils informatiques développés pour traiter les données génomiques du fragment étudié. 
Tous les programmes sont écrits en Python et conçus pour être utilisés en ligne de commande avec des arguments dynamiques.

## Présentation des programmes
1. `use_scan_for_matches.py`
   
Ce script est l'interface permettant de contrôler la recherche de motifs biologiques comme les RBS, les promoteurs, les terminateurs ou encore pour des recherches personnalisées. Son rôle principal est de lancer les recherches de motifs basées sur les matrices de _B.subtilis_. Concernant son fonctionnement, il génère les fichiers de résultats bruts qui serviront ensuite d'entrée à notre parser universel.

2. `convertisseur.GFF.py` (Conversion GeneMark vers GFF)
   
Ce programme est un outil qui transforme les sorties de GeneMark en format LST en format standard GFF. Il possède une logique d'auto-détection capable de distinguer si le fichier provient de GeneMark classique ou de GeneMark.hmm dès la lecture de la première ligne. Pour les fichiers LST, le script gère précisément les débuts alternatifs en utilisant un système de compteurs pour identifier chaque CDS et ses versions, par exemple GM_CDS_1.1, dans la colonne note. Enfin, le script calcule et génère automatiquement les coordonnées des codons initiateurs (feature ATG) pour chaque prédiction traitée

3. `convertisseur_sfm_GFF.py` (Parser Universel)
Il s'agit d'un programme conçu pour traiter n'importe quel résultat issu de l'outil scan_for_matches. Sa flexibilité repose sur l'utilisation d'arguments en ligne de commande : l'utilisateur précise le type de motif recherché (RBS, promoteur, terminateur), ce qui permet au script de l'inscrire dynamiquement dans la colonne feature du GFF. Le script calcule automatiquement le brin (+ ou -) en comparant les positions de début et de fin. Une fonctionnalité spécifique a été ajoutée pour les RBS : si cette feature est détectée, le programme génère immédiatement une ligne supplémentaire pour positionner le codon ATG associé.
