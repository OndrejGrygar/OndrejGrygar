def greatest_common_divisor(a, b):
    biggest = 0
    for i in range(1, a + b):
        if a % i == 0 and b % i == 0:
            biggest = i
    return biggest





print(greatest_common_divisor(24, 36))
print(greatest_common_divisor(7, 27))
print(greatest_common_divisor(48, 64))
print(greatest_common_divisor(48, 65))