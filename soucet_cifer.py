def digit_sum(n):
    prevod = list(str(n))
    soucet = 0
    prevod = [int(i) for i in prevod]
    for x in prevod:
       soucet += x
    return soucet



print(digit_sum(125))
print(digit_sum(58))
print(digit_sum(415458))