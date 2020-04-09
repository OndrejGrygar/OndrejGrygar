def fibonacci(n):
    n1, n2 = 1, 1
    count = 0
    while count < n:
        print(n1)
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1

fibonacci(10)

