numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print (f"O número {numero} é PAR")
else:
    print(f"O número {numero} é ÍMPAR")

if numero >0:
    print ("O número é Positivo")
elif numero <0:
    print (" O número é Negativo")
else:
    print ("O número é Zero")
