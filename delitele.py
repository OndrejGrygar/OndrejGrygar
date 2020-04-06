def divisors_count(n):
    pocet = 0
    for i in range(n+1):
        if i == 0:
            continue
        if n % i == 0:
            pocet += 1

    return pocet


print(divisors_count(24))