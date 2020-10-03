#!/usr/bin/env python3


#colocar numeros inteiros positivos

# a_str e b_str guardam strings
a_str = int(input("Numero de a: "))
if a_str > 0 and a_str < 1000:
	a_str = a_str
	print(a_str)

else:
	print("Não está entre 0 e 1000")
	

b_str = int(input("Numero de b: "))
if b_str > 0 and b_str < 1000:
        b_str = b_str
        print(b_str)

else:
        print("Não está entre 0 e 1000")

# é referente ao numero ao quadrado da raiz hipotenusa
x = a_str * a_str + b_str * b_str
print(x)



