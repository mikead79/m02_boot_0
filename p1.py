def sumaTodos(limitTo):
    resultado = 0
    for i in range(limitTo+1):
        resultado += i
    return resultado

print(sumaTodos(100))