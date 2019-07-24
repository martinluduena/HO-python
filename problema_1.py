a = range(0,1000,3) #defined as a list
b = range(0,1000,5)
c = set(a) | set(b) #redefined as a set and union
print (c)

def sumar_elementos(Xs):
    suma=0
    for i in Xs:
        suma=suma+i
    return suma

print (sumar_elementos(c))

