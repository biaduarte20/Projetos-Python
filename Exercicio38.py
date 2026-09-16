maior = None
menor = None

for i in range(100):
    numero = float(input("Digite um número positivo: "))

    if numero > 0:
        if maior is None or numero > maior:
            maior = numero

        if menor is None or numero < menor:
            menor = numero

print("Maior:", maior)
print("Menor:", menor)
