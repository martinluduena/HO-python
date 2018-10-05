# Si hacemos una lista de todos los números naturales debajo de 10 que sean 
# múltiplos de 3 o 5 obtendríamos 3, 5, 6 y 9. La suma de los múltiplos es 23.
# Encuentre la suma de todos los múltiplos de 3 y 5 debajo de 1000.

a = range(0,1000,3) #defined as a list
b = range(0,1000,5)
c = set(a) | set(b) #redefined as a set and union
print c
print sum(c)
