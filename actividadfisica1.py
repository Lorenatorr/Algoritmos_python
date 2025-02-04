
minutos_diarios = []
print("Ingrese la cantidad de minutos de ejercicio realizado cada día de la semana:")
for i in range(7):
    minutos = int(input(f"Día {i + 1}: "))
    minutos_diarios.append(minutos)

for i, minutos in enumerate(minutos_diarios):
    if minutos > 90:
        print(f"Día {i + 1}: Felicitaciones, has hecho {minutos} minutos de ejercicio. ¡Gran trabajo!")
        print("Recuerda no exceder los 90 minutos para evitar posibles riesgos de salud.")

total_semanal = sum(minutos_diarios)

print("\n Resultados Semanales ")
print(f"Total de minutos de ejercicio durante la semana: {total_semanal} minutos")

if total_semanal >= 150:
    print("¡Felicitaciones! Has alcanzado el objetivo semanal de actividad física. ¡Sigue así!")
else:
    print("No alcanzaste el objetivo de 150 minutos semanales. Te sugerimos incrementar tu actividad física.")

