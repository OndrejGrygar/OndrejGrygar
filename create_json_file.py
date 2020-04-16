import json

idcust1 = {
    "firstname": "Ondrej",
    "lastname": "Grygar",
    "age": 29,
}
with open("idcust1.json", "w") as file:
    json.dump(idcust1, file)