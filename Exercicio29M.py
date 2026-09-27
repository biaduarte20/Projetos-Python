def entrada():
    tipo = int(input("Digite o tipo de investimento (1 - Poupança / 2 - Renda Fixa): "))
    valor = float(input("Digite o valor do investimento: R$ "))

    return tipo, valor


def calcular_investimento(tipo, valor):
    if tipo == 1:
        valor_corrigido = valor * 1.03

    elif tipo == 2:
        valor_corrigido = valor * 1.05

    return valor_corrigido


def saida(tipo, valor_corrigido):
    if tipo == 1 or tipo == 2:
        print(f"Valor corrigido após 30 dias: R$ {valor_corrigido:.2f}")

    else:
        print("Tipo de investimento não considerado.")


def main():
    tipo, valor = entrada()
    
    if tipo == 1 or tipo == 2:
        valor_corrigido = calcular_investimento(tipo, valor)
        saida(tipo, valor_corrigido)

    else:
        saida(tipo, valor)


main()