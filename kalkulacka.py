def soucet(x, y):
    return x + y
def odecet(x, y):
    return x - y
def nasobeni(x, y):
    return x * y
def deleni(x, y):
    return x / y

print("zvol si funkci kalkulacky:")
print("1 : soucet")
print("2: odecitani")
print("3: nasobeni")
print("4: deleni")

vyber = int(input("Zvol 1| 2| 3| 4| :"))
num1 = int(input("Zadej prvni cislo:"))
num2 = int(input("Zadej druhe cislo:"))

if vyber == 1:
    print("Soucet cisel ", num1, "+" , num2," = ",soucet(num1, num2))
elif vyber == 2:
    print("Odecitani cisel ",num1 , "-", num2, " = ", odecet(num1, num2))
elif vyber == 3:
    print("Nasobeni cisel ",num1 , "*", num2, " = ", nasobeni(num1, num2))
elif vyber == 4:
    print("Deleni cisel ", num1, "/", num2, " = ", deleni(num1, num2))