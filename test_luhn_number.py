def luhn(num):
    num_str = str(num).replace(' ', '')
    num = num_str[::-1]

    s1 = 0
    s2 = 0
    for index,value in enumerate(num):
        if index % 2 == 0:
            s1 += int(value)
        else:
            value = int(value) * 2
            if value > 9:
                value = int(str(value)[0])+ int(str(value)[1])
            s2 += int(value)

    print(s1 + s2)
    result = True if (s1 + s2) % 10 == 0 else False

    return result

print(luhn(49927398716))