horas_trabalhadas = float(input("Digite as horas trabalhadas: "))
valor_hora = float(input("Digite o valor por hora: R$ "))
percentual_desconto = float(input("Digite o percentual de desconto: "))
num_dependentes = int(input("Digite o numero de dependentes: "))

salario_bruto = horas_trabalhadas * valor_hora
valor_desconto = salario_bruto * (percentual_desconto / 100)
salario_liquido = salario_bruto - valor_desconto

salario_final = salario_liquido + (num_dependentes * 100)

print(f"Salario Bruto a receber: R$ {salario_bruto:.2f}")
print(f"Salario a receber: R$ {salario_final:.2f}")