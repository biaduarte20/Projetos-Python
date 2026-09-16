a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

if a > b:
    inicio = b
    fim = a
else:
    inicio = a
    fim = b

soma = 0

for i in range(inicio, fim + 1):
    if i % 2 != 0:
        soma += i

print("Soma dos ímpares:", soma)
