a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

if a > b:
    inicio = b
    fim = a
else:
    inicio = a
    fim = b

for numero in range(inicio, fim + 1):
    if numero >= 2:
        primo = True

        for divisor in range(2, numero):
            if numero % divisor == 0:
                primo = False
                break

        if primo:
            print(numero)
