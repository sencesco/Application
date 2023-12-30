import pandas as pd

data = pd.read_csv("data/WordFrequency_English.csv")

data_eng = data["lemma"]
print(data_eng)

data_eng.to_csv("data/WordFrequency_English.csv")

""" with open("data/WordFrequency_English.csv", "w") as rewrite_file:
    data_eng. """
    