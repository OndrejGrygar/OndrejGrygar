def print_products(n):
    for i in range(n+1):
        if i == 0:
            continue
        elif n % i == 0:
            print(n, "=", i , "*", int(n/i))

print_products(36)