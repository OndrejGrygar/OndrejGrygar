def print_primes(n):
    counts = 0
    for num in range(2,100):
        if counts < n:
            for i in range(2,num):
                if (num % i) == 0:
                    break
            else:
                print(num)
                counts += 1
print_primes(10)