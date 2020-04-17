import csv

with open("potions.csv") as f:
    contents = csv.reader(f)
    potter_comp = []
    for eachline in contents:
        potter_comp += eachline
index_of_item = potter_comp.index("Draught of Peace")
print(potter_comp)
print(index_of_item)