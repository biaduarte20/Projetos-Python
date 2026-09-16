tipo = int(input("Digite o tipo de investimento (1-Poupança / 2-Renda Fixa): "))
valor = float(input("Digite o valor do investimento: "))

if tipo == 1:
    valor_corrigido = valor * 1.03
    print("Valor corrigido: R$", valor_corrigido)
elif tipo == 2:
    valor_corrigido = valor * 1.05
    print("Valor corrigido: R$", valor_corrigido)
else:
    print("Tipo de investimento inválido.")
