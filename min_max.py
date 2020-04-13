def my_min(list):
    min = list[0]
    for i in list[1:]:
        if i < min:
            min = i
    return min


my_min([43,45,87,21,23])
