sentence = 'A speech sound that is produced by comparatively open configuration of the vocal tract.'

samohlasky = "aeiouy"

pocty = {"samo":0,"sou":0}

for letter in sentence:
    if not letter.isalpha():
        continue
    if letter.lower() in samohlasky:
        pocty["samo"] += 1
    else:
        pocty["sou"] += 1
print("No. Samohlasek: ", str(pocty["samo"]), "| No. Souhlasek: ", str(pocty["sou"]))