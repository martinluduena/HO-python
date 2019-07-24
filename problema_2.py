def fib(n):
    a,b = 0,1
    lista_fib = []
    while a < n:
        #print (a, end=' ')
        a,b = b,a+b
        lista_fib.append(b)
    #print()
    return lista_fib
	
lista = fib(100)

def sumalista(lista):
    suma=0
    for i in lista:
        if i%2 != 0:
            suma=suma+i      
    return suma

print(sumalista(lista))


   
