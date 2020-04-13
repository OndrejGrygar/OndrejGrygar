def my_count(predmet, list):
    pocet = 0
    predmet = predmet.lower()
    for item in list:
        item = item.lower()
        if item == predmet:
            pocet += 1
    return pocet


names = ['Rob', 'Jim', 'Mark', 'Mark', 'Mark', 'Bob', 'Mark', 'Bob', 'Bob', 'Rob', 'Jim', 'Mark', 'Mark', 'Bob',
             'Mark']
print(my_count("Bob", names))