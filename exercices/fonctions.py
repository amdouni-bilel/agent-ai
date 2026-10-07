def saluer(prenom):
    return f"Bonjour {prenom}, bienvenue!"


def calculer_prix(nb_participants, nb_jours, prix_jour=350): 
    return nb_participants * nb_jours * prix_jour


message = saluer("Amira")
print(message)

print(calculer_prix(3, 3))
print(calculer_prix(3, 3, prix_jour=400))