import pandas as pd


# Étape 1 bis : explorer
clients = pd.read_csv("clients.csv")
print(clients.head())
print("Dimensions :", clients.shape)

print(clients.isna().sum())
print("Doublons avant le nettoyage :", clients.duplicated().sum())

clients = clients.drop_duplicates() 
mediane = clients["montant_moyen"].median() 
clients["montant_moyen"] = clients["montant_moyen"].fillna(mediane) 
print("Après nettoyage :", clients.shape) 
print("Valeurs manquantes restantes :", clients.isna().sum().sum())

print(clients.isna().sum())
print("Doublons après le nettoyage :", clients.duplicated().sum())