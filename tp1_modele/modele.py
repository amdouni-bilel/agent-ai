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


from sklearn.model_selection import train_test_split


X = clients[
    ["anciennete_mois", "nb_achats", "montant_moyen", "reclamations"]
]

y = clients["a_quitte"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Exemples pour l'entraînement :", len(X_train))
print("Exemples pour le test :", len(X_test))


# Étape 2 : entraîner le modèle
from sklearn.tree import DecisionTreeClassifier

modele = DecisionTreeClassifier(
    max_depth=3,
    random_state=42
)
modele.fit(X_train, y_train)
print("Modèle entraîné !")


# Étape 3 : évaluer le modèle
from sklearn.metrics import accuracy_score, confusion_matrix


predictions = modele.predict(X_test)

precision = accuracy_score(y_test, predictions)

print(f"Taux de bonnes réponses : {precision:.0%}")

print("Matrice de confusion :")
print(confusion_matrix(y_test, predictions))

from sklearn.tree import export_text


print(export_text(
    modele,
    feature_names=list(X.columns)
))

importances = pd.Series(
    modele.feature_importances_,
    index=X.columns
).sort_values(ascending=False)

print(importances.round(2))


# Étape 4 : predire le modèle
nouveaux_clients = pd.DataFrame({
    "anciennete_mois": [3, 48],
    "nb_achats": [2, 25],
    "montant_moyen": [90.0, 210.0],
    "reclamations": [4, 0],
})

resultats = modele.predict(nouveaux_clients)
probas = modele.predict_proba(nouveaux_clients)

for i in range(len(nouveaux_clients)):
    decision = "VA PARTIR" if resultats[i] == 1 else "reste fidèle"

    print(
        f"Client {i + 1} : {decision} "
        f"(probabilité de départ : {probas[i][1]:.0%})"
    )


import joblib 
joblib.dump(modele, "modele_clients.pkl") 
print("Modèle sauvegardé dans modele_clients.pkl")


# Ameliorer modele 

## Étape 1 : charger les données
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression


# Random Forest
foret = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

foret.fit(X_train, y_train)

print(
    f"Random Forest : "
    f"{accuracy_score(y_test, foret.predict(X_test)):.0%}"
)


# Régression logistique
logistique = LogisticRegression(
    max_iter=1000
)

logistique.fit(X_train, y_train)

print(
    f"Régression logistique : "
    f"{accuracy_score(y_test, logistique.predict(X_test)):.0%}"
)

