import pandas as pd

df_poke = pd.read_csv("pokemon_data.csv", sep = ",") # charge le tableau csv dans la variable df_poke



###Afficahege de base ###

#print(df_poke.head(3)) # affiche les 3 premieres lignes 
#print(df_poke.tail(3)) # affiche les 3 dernieres lignes 
#print(df_poke["Name"][10:50]) #affiche du 10eme au 50eme element de la colonne Name 
#print(df_poke[["Name","HP"]]) #python crée une liste a partir des colonnes a afficher d'ou le double crochet 
#print(df_poke.iloc[1]) #iloc[] indique que l'ont veut la ligne /!\ iloc ne compte pas la ligne d'en tete 
#print(df_poke.iloc[2,1]) # 2eme ligne, 1ere colonne 
### iloc donne un resultat en fonction d'un indice, iloc[1] donnera toujours le truc situé a la position 1; loc donne un resultat en fonction d'un nom, loc[1] cherchera un truc qui s'appelle 1
#print(df_poke.sort_values(["HP"], ascending=1).head(10))
#print(df_poke.sort_values("Name", ascending=True))
#print(df_poke.sort_values(["Type 1", "HP"],ascending=[False,True]))



###Conditionnement ###

#for index,row in df_poke.iterrows(): #iterrows a besoin d'une paire de valeurs (ligne (index) + colonne (row)), et cela veut dire sur toute les lignes 
 #   if row["HP"] > 80 :  #si dans la colonne row il y a plus de 80 alors :
#        print(row["Name"],row["HP"])
#print(df_poke.loc[df_poke["Type 1"] == "Fire"])
#print(df_poke.loc[(df_poke["HP"] > 80) | (df_poke["Type 1"] == "Grass")]) #la barre signifie OU et les conditions se mettent entre parentheses quand il y en a plusieurs, "et" s'écrit "&"
#print(df_poke.loc[df_poke["Name"].str.contains("Mega")]) #la maniere de l'écrire est super confusante mais c'est comme ca qu'on fait pour chercher un contenu 
#print(df_poke.loc[~df_poke["Name"].str.contains("Mega")]) #alors la j'ai 0 explication "inverse" c'est "~"




###Modifications ###

#df_poke["Total"] = df_poke["HP"] + df_poke["Attack"] + df_poke["Defense"] + df_poke["Sp. Atk"] + df_poke["Sp. Def"] + df_poke["Speed"] #ajout d'une colonne 
#cols = list(df_poke.columns)
#print(df_poke[cols[0:4] + [cols[-1]] + cols[4:12]]) #change l'ordre des colonnes, la colonne unique doit etre entre crochets 
#df_poke.to_csv("nom_du_fichier",index = False) #sauvegarde l'actuel df_poke au nom spécifié au format csv, on peut choisir le format facilement 
#.reset_index(drop = True) #permet de recréer un index qui commence a 0 et fini a n = nb de lignes, ca fait souvent plus propre 
#df_poke.loc[(df_poke["Type 1"] == "Fire") , "Type 1"] = "Flammer" #Hérésie, mais c'est comme ca que l'on remplace des trucs 
#df_poke.loc[df_poke["Type 1"] == "Fire" , "Legendary"] = "True" #on peut utiliser une condition sur une colonne pour en modifier une autre 
#df_poke.loc[df_poke["Type 1"] == "Fire" , ["Legendary", "Type 2"]] = ["True" , "Bug"] #on peut changer plusieurs trucs aussi /!\ le double crochet ferme se met aux valeurs a changer 
#df_poke = df_poke.drop(df_poke[df_poke['Type 1'] == 'Grass'].index) #supprimer des lignes en fonction d'une condition 


###Info statistiques 

#print(df_poke.describe()) #donne des informations statistiques sur le data frame 
#print(df_poke.groupby(["Type 1"])[["HP","Attack","Defense","Sp. Atk", "Sp. Def", "Speed"]].mean()) #donne les moyenne en fonction des contenu de la colonne "Type 1"
#print(df_poke.groupby(["Type 1"])[["HP","Attack","Defense","Sp. Atk", "Sp. Def", "Speed"]].mean().sort_values("Defense",ascending=False)) #on peut rajouter des trucs 
#print(df_poke.groupby(["Type 1"]).count()) #ca compte en fonction du type 1
#print(df_poke.groupby(["Type 1","Type 2"]).count()) #ca crée des sous ensembles 