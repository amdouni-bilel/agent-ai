# Question de l'utilisateur
question = "calcul 12 * 350"

# Déterminer la route selon la question
if question == "Bonjour":
    print("Route : salutation")

elif "calcul" in question:
    print("Route : calculatrice")

else:
    print("Route : recherche dans les documents")