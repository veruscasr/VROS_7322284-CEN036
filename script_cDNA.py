#!/usr/bin/env python3

import sys

#argumentos e Verificar numeros em relação ao tamanho do DNA

sequencia_DNA = sys.argv[1] #isso é uma string
n1 = int(sys.argv[2])
n2 = int(sys.argv[3])
n3 = int(sys.argv[4])
n4 = int(sys.argv[5])

#A função len() serve para calcular o comprimento de uma string. Esta função recebe uma sequência como argumento e retorna um int

if n1 > len(sequencia_DNA):
        print("N1 é maior que a quesencia de DNA, inserir valor menor")
elif n2 > len(sequencia_DNA):
        print("N2 é maior que a quesencia de DNA, inserir valor menor")
elif n3 > len(sequencia_DNA):
        print("N3 é maior que a quesencia de DNA, inserir valor menor")
elif n4 > len(sequencia_DNA):
        print("N4 é maior que a quesencia de DNA, inserir valor menor")
else:
        print("Os valores estão corretos")

#Extraindo sequencia da CDS 1 e conferir se inicia com o códon de inicio, ATG.

CDS_1 = sequencia_DNA[n1-1:n2]
print(CDS_1)

#Extraindo sequencia da CDS 2 e conferir se termina com um dos códons de parada, TAG, TAA ou TGA.

CDS_2 = sequencia_DNA[n3-1:n4]
print(CDS_2)

#Conferir se CDS 1 inicia com código de início ATG

if CDS_1[0:3] in "ATG":
    print("É um códon de inicio")
else:
    print("O Códon não é de início")

#Conferir se CDS 2 termina com um dos códons de parada  TAA,TAG ou TGA

if CDS_2[-3] in "ATG":
    print("É um códon de inicio")
else:
    print("O Códon não é de início")


#Caso o ponto 3 e 4 sejam verdadeiros, imprimir na tela a sequencia que resulta da juntar (concatenar) as CDS 1 e CDS 2.
arg_3 = CDS_1
arg_4 = CDS_2

if arg_3 and arg_4:
    seq_concatenada = CDS_1 + CDS_2
    print("Sequencia concatenada", (seq_concatenada))
else:
    print("A sequência não foi concatenada")

