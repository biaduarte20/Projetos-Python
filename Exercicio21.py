n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

media = (n1 + n2 + n3 + n4) / 4

print("Média:", media)

if media >= 6:
    print("APROVADO")
elif media >= 3:
    print("EXAME")
else:
    print("RETIDO")
