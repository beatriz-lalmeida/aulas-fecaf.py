compra = float(input("Digite o valor da compra: "))
idade = int(input("Digite a sua idade: "))
estudante = str(input("Você é estudante? "))

if compra >= 500 and idade >= 60:
    desconto = 15
elif compra >= 500 or estudante == "sim":
    desconto = 10
elif compra >= 200:
    desconto = 5 
else: print ("Sem desconto")

porcentagem = compra * desconto/100
valor_final = compra - porcentagem

print(f"O seu percentual de desconto é {desconto} %")
print (f"O valor final da compra é de {valor_final} reais")
