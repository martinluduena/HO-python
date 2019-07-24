numero = 600851475143
numero = numero*1993
numero = numero*3
n = numero  # Variable auxilair
div = 2     # divisor, inicializo con div = 2

l_div = [] # lista de numeros primos, factores de numero

while n > 1:
    if n%div == 0:         # Significa que div es un factor de n.\n",
        l_div.append(div)  # agrego div a la lista de factores primos de n\n",
        n = n / div        # Asigno el valor de la divición a n, para evitar contar factores compuestos de n.\n",
    else:
        div += 1        

print(l_div)
