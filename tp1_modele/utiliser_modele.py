import joblib
import pandas as pd


# Charger le modèle
modele = joblib.load("modele_clients.pkl")


# Créer les données du nouveau client
client = pd.DataFrame({
    "anciennete_mois": [12],
    "nb_achats": [5],
    "montant_moyen": [120.0],
    "reclamations": [3],
})


# Effectuer la prédiction
print("Prédiction :", modele.predict(client)[0])

