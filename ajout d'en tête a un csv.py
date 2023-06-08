import csv

chemin_fichier = "C:\\Users\\tsalv\\Desktop\\python\\convertisseur\\adults.csv" # chemin vers le fichier 
en_tete = ["age", "workclass", "fnlwgt", "education", "education-num", "marital-status", "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss", "hours-per-week", "native-country"]
#en tete a rajouter

with open(chemin_fichier, 'r+', newline='') as fichier_csv:
    lignes = list(csv.reader(fichier_csv))#on rentre le fichier csv dans une variable
    lignes.insert(0, en_tete) #on ecrase la premiere ligne avec notre en tete 
    ecrire = csv.writer(fichier_csv) #on va écrire dans le fichier csv (méthode writer)
    ecrire.writerows(lignes) # on réécrit dans le fichier csv apres l'en tête 