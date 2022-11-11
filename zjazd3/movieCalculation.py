import math
'''
Function for calculating cosine similarity between users
'''
def cosine_dic(dic1,dic2):
    numerator = 0
    dena = 0
    for key1, val1 in dic1.items():
        numerator += val1*dic2.get(key1, 0.0)
        dena += val1*val1
    denb = 0
    for val2 in dic2.values():
        denb += val2*val2
    return numerator/math.sqrt(dena*denb)

'''
Function for creating lists containing movies for recommendation
'''
def make_list(list1,list2,list3):
    keys1 = []
    keys2 = []
    for i in (list1):
        keys1.append(list(i.keys()))
    for g in (list2):
        keys2.append(list(g.keys()))
    for h in keys1:
        if h not in keys2:
            list3.append(h)
    return list3

'''
Function for cleaning lists in case of shared movies with different scores
'''
def cleaner(lista1,lista2):
    for element in lista1:
        if [element] in lista2:
            lista2.remove([element])
    return lista2