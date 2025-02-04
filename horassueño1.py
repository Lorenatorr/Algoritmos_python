horas_sueno = []

print("Ingrese las horas de sueño de cada noche durante 7 días:")
for i in range(7):
    horas = float(input(f"Noche {i + 1}: "))
    horas_sueno.append(horas)

promedio_semanal = sum(horas_sueno) / len(horas_sueno)

for i, horas in enumerate(horas_sueno):
    if horas < 5:
        print(f"Noche {i + 1}: Dormiste {horas:.1f} horas. Es necesario mejorar este hábito.")

print(f"Promedio semanal de sueño: {promedio_semanal:.2f} horas")

if promedio_semanal < 7:
    print("Recomendación: Procura dormir más horas para mejorar tu salud y bienestar.")
else:
    print("¡Felicitaciones! Tienes buenos hábitos de sueño.")
