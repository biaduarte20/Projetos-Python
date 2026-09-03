alimentos_kg = float(input("Digite a quantidade de alimentos em quilos: "))

consumo_diario_kg = 0.5

dias_duracao = alimentos_kg / consumo_diario_kg

print(f"O alimento durará {int(dias_duracao)} dias.")