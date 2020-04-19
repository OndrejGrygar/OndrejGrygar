#Otestuj jestli jsou zadana slova anagramy
def all_anagrams(x):
    if x:
        result = True
        word_sorted = sorted(x.pop())
        for word in x:
            if sorted(word) != word_sorted:
                result = False
            else:
                result = True
    else:
        result = false
    return result



print(all_anagrams(['ship','hips']))

