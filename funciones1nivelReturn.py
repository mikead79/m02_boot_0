def maxi(*l):
    if len(l) == 0:
        return 0
    m = l[0]
    for elemento in l:
        if m < elemento:
            m = elemento
    return m

def mini(*l):
    if len(l) == 0:
        return 0
    m = l[0]
    for elemento in l:
        if m > elemento:
            m = elemento
    return m

def media(*l):
    if len(l) == 0:
        return 0
    m = 0
    for elemento in l:
        m += elemento
    return m/len(l)

funciones = {
    "max": maxi,
    "min": mini,
    "med": media
    }

def returnF(nombre):
    nombre = nombre.lower()
    if nombre in funciones:
        return funciones[nombre]
    return None

