def collatz(number):
    if number % 2 == 0:
        print(number//2)
        return number//2
    else:
        print(3 * number + 1)
        return 3 * number + 1

while True:
    try:
        inserted_num = int(input("Insert a number:"))
        #collatz(inserted_num)
        if collatz(inserted_num) == 1:
            break
    except Exception:
        print("Inserted value isnt number")

