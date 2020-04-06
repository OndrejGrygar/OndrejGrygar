TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]
registered_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123",
}# uklada do slovniku kombinace Uzivatel:Heslo
print("-"* 40)
print("Welcome !!! ")
print("Please LOG IN ")
i = True # uklada boolean hodnotu do i, potrebuji ji k smycce while
while i == True: # kdyz je i rovna True .. probiha zbytek pod while, kdyz je radek odsazen
    username = input("Username: ")
    password = input("Password: ")

    if registered_users.get(username) != password: # ve while vlozena podminka
        print("wrong username or password") #kdyz username nematchuje s heslem vypise zpravu
    else: # kdyz if neni splneno, a username: heslo matchuje
         i = False # zmeni i na False a tim While konci
# jinak zapsana podminka
#for key, value in registered_users.items():
   # if key == username and value == password:
    #    print("You are logged")
     #   break
    #else:
     #   print("Wrong Username or Password")

print("-" * 40)

choice = int(input("Zadej 1, 2 nebo 3!podle toho, ktery text chce analyzovat:"))
print("-" * 40)

text = TEXTS[choice- 1] # ulozeni do nove var text vyber uzivatlele se spravnym indexem,

words = text.split() # rozdeleni text na jednotliva slova , utvori list

print(choice, ".text ma ", len(words), "slov.") # vypis poctu slov v textu

print("-" * 40)

words1 = [] # vytvoreni noveho listu

while words:
    word = words.pop() #vyhazuje ze seznamu words, jednotliva slova
    word = word.strip(".,:/;") #ocistuje slovo od danych znaku
    if word: words1.append(word) #pridava slova do listu

titlecase = 0 #vytvarim var pro vsechny skupiny,ktere chci zjistit
lowercase = 0
uppercase = 0
numeric = 0

x = 0

while x < len(words1): # opakovani dokud x bude mensi jako delka listu words1
    if words1[x].istitle():
        titlecase += 1
    elif words1[x].islower():
        lowercase += 1
    elif words1[x].isupper():
        uppercase += 1
    elif words1[x].isnumeric():
        numeric += 1

    x += 1

print("Mame ", titlecase, " slov s pocatecnim velkym pismenem")
print("Mame ", lowercase, " slov psanych malym pismem")
print("Mame ", uppercase, " slov psanych velym pismem")
print("Mame ", numeric, " cisel v textu")

print("-" * 40)
