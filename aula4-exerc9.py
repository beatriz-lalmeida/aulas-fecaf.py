N1 = float(input("Digite a primeira nota: "))
N2 = float(input("Digite a segunda nota: "))
N3 = float(input("Digite a terceira nota: "))
media = round((N1 + N2 + N3) /3,2)
print (f"A media das tres notas e {media}")

if media >=5.0 and media <7.0:
  print ("Recuperacao")
elif media >=7:
  print ("Aprovado")
else:
  print ("Reprovado")