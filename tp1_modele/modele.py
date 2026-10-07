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