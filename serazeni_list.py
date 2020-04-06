names = ['Michal', 'Pepa', 'Honza',
        'Pavel', 'Lukas', 'Matej',
        'Iva', 'Klara', 'Jana',
        'Honza', 'Vasek','Milan', 'Michal']
sorted_names = [names.pop(0)]

for name in names:
    for i,name2 in enumerate(sorted_names):
        if name < name2:
            sorted_names.insert(i,name)
            break
    else:
        sorted_names.append(name)
print(sorted_names)