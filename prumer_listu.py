'''
def mean(list):
    soucet = 0
    for i in list:
        soucet += i
    result = soucet / len(list)
    return result
'''
def mean(list):
    return sum(list)/len(list)

print(mean([32,43,54,54,76,21,62,83,52,58]))