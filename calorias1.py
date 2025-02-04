calorias_diarias = []

print("Ingrese las calorías consumidas cada día de la semana:")
for i in range(7):
    calorias = int(input(f"Día {i + 1}: "))
    calorias_diarias.append(calorias)

promedio_semanal = sum(calorias_diarias) / len(calorias_diarias)


dias_altas_calorias = []
for i, calorias in enumerate(calorias_diarias):
    if calorias > 2500:
        dias_altas_calorias.append(i + 1)

print("\nResultados")
print(f"Calorías diarias: {calorias_diarias}")
print(f"Promedio semanal de calorías: {promedio_semanal:.2f} calorías")

if dias_altas_calorias:
    print("Advertencia: Los siguientes días se consumieron más de 2500 calorías:")
    for dia in dias_altas_calorias:
        print(f"  - Día {dia}")

if promedio_semanal > 2000:
    print("Advertencia: Ha superado la ingesta calórica recomendada de 2000 calorías diarias en promedio.")
else:
    print("Buen trabajo: Está dentro del rango calórico recomendado.")
