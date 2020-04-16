import csv

with open("file.csv", "w", newline="") as new_file:
    content = csv.writer(new_file, delimiter=",")
    content.writerow(["year", "winner", "event"])
    content.writerow([1990, "Brazil", "World Cup"])