import pandas as pd


# Étape 1 bis : explorer
clients = pd.read_csv("clients.csv")
print(clients.head())
print("Dimensions :", clients.shape)
