nota = float(input("Digite a nota: "))
frequencia = float(input("Digite a frequência: "))

if nota >= 9 and frequencia >= 90:
    print ("Excelente")
elif nota >= 7 and frequencia >= 75:
    print ("Bom")
elif nota >= 5 and frequencia >= 75:
    print ("Regular")
else:
    print("Insuficiente")
