salario_bruto = float(input("Digite o salário bruto: "))

if salario_bruto <=2259.20:
  aliquota = 0
  desconto = 0.00
elif salario_bruto <=2826.65:
  aliquota = 7.5
  desconto = 169.44
elif salario_bruto <=3751.05:
  aliquota = 15
  desconto = 381.44
elif salario_bruto <=4664.68:
  aliquota = 22.5
  desconto = 662.77
else:
  aliquota = 27.5
  desconto = 896.00

imposto = salario_bruto * (aliquota / 100) - desconto
salario_liquido = salario_bruto - imposto

print (f"Seu salario bruto e de {salario_bruto} reais")
print (f"Sua aliquota e de {aliquota}%")
print (f"Seu imposto e de {imposto:.2f} reais")
print (f"Seu salario liquido e de {salario_liquido:.2f} reais")