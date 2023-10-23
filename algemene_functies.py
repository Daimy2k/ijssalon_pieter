def mijn_functie_1(a=0):
    return a ** 2

print(mijn_functie_1(12))


def mijn_functie_2(a,b):
    teruggeefwaarde=[]
    teruggeefwaarde.append(a + b)
    teruggeefwaarde.append(a - b)
    teruggeefwaarde.append(a * b)
    teruggeefwaarde.append(a / b)
    return teruggeefwaarde
print(mijn_functie_2(100,20))