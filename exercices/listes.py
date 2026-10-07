# Création d'une liste de documents
documents = ["rh.txt", "procedure.pdf", "formation.docx"]

# Accès aux éléments de la liste
print(documents[0])
print(documents[-1])

# Nombre de documents
print(len(documents))

# Ajouter un nouveau document
documents.append("contrat.txt")

# Afficher la liste mise à jour
print(documents)

# Parcourir la liste
for doc in documents:
    print("Lecture du fichier :", doc)