deposito = float(input("Digite o valor do depósito: R$ "))

rendimento = 0.013
valor_final = deposito * (1 + rendimento)

print(f"Valor após 1 mês: R$ {valor_final:.2f}")
