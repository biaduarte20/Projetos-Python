def entrada():
    preco_atual = float(input("Digite o preço atual: R$ "))
    venda_mensal = int(input("Digite a média mensal de vendas: "))

    return preco_atual, venda_mensal


def calcular_preco(preco_atual, venda_mensal):
    preco_novo = preco_atual

    if venda_mensal < 500 and preco_atual < 30:
        preco_novo = preco_atual * 1.10

    elif venda_mensal >= 500 and venda_mensal < 1000:
        if preco_atual >= 30 and preco_atual < 80:
            preco_novo = preco_atual * 1.15

    elif venda_mensal >= 1000 and preco_atual >= 80:
        preco_novo = preco_atual * 0.95

    return preco_novo


def saida(preco_novo):
    print(f"Novo preço: R$ {preco_novo:.2f}")


def main():
    preco_atual, venda_mensal = entrada()
    preco_novo = calcular_preco(preco_atual, venda_mensal)
    saida(preco_novo)


main()
