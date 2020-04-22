def list_primes(n):
    nums = list(range(2, n+1))
    result = []

    while nums:
        i = nums.pop(0)
        result.append(i)
        for num in nums:
            if num % i == 0:
                nums.remove(num)
    return result






def is_prime(n):
    if n in list_primes(n):
        print("Yes")
    else:
        print("NO")
is_prime(11)