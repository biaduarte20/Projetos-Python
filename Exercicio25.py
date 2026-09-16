hora_inicio = int(input("Hora de início: "))
min_inicio = int(input("Minuto de início: "))

hora_final = int(input("Hora de final: "))
min_final = int(input("Minuto de final: "))

inicio = hora_inicio * 60 + min_inicio
fim = hora_final * 60 + min_final

if fim <= inicio:
    fim += 24 * 60

duracao = fim - inicio

horas = duracao // 60
minutos = duracao % 60

print("Duração:", horas, "hora(s) e", minutos, "minuto(s)")
