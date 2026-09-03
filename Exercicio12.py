ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

idade_atual = ano_atual - ano_nascimento
idade_futura = idade_atual + 17

print(f"Sua idade atual é: {idade_atual} anos")
print(f"Daqui a 17 anos você terá: {idade_futura} anos")