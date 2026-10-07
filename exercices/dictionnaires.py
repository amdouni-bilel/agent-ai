# Création d'un dictionnaire représentant un employé
employe = {
    "nom": "Sami",
    "poste": "Technicien",
    "conges": 30,
}

# Accéder à une valeur
print(employe["nom"])

# Utiliser get() avec une valeur par défaut
print(employe.get("salaire", "non renseigné"))

# Ajouter une nouvelle information
employe["service"] = "Maintenance"

# Afficher le dictionnaire mis à jour
print(employe)

# Parcourir les clés et les valeurs
for cle, valeur in employe.items():
    print(cle, "→", valeur)