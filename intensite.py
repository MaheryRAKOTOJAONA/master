#!/usr/bin/env python3
import os, sys, re

if len(sys.argv)<2:
    print("Il n'y a pas d'argument")
    sys.exit(1)

# Récupère le pas en 2e argument si présent, sinon 10 par défaut
pas = int(sys.argv[2]) if len(sys.argv) >= 3 else 10

spectre= os.path.expanduser(sys.argv[1])
i=0
lecture=False
FenetreLongueurOnde={}


if os.path.isfile(spectre):
    with open (spectre, "r", encoding="utf-8") as fichier:
        for ligne in fichier:
            if "Begin Spectral Data" in ligne:
                lecture=True
                continue
            if "End Spectral Data" in ligne:
                lecture=False
                break
            if lecture==True:
                liste=re.findall(r"-?\d+\.?\d*", ligne)
                if len(liste)>=2:
                    longueurOnde=float(liste[0])
                    intensite=float(liste[1])

                    #Definition du pas
                    debut=int(longueurOnde//pas)*pas
                    cle=(debut, debut+pas)

                    if cle not in FenetreLongueurOnde:
                        FenetreLongueurOnde[cle]=[]
                    FenetreLongueurOnde[cle].append(intensite)

                i+=1
    
        print(i)
else:
    print("fichier introuvable")
    sys.exit(1)
print (FenetreLongueurOnde)