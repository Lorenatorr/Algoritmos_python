minutos_ejercicio = []


for dia in range(7):
    minutos = int(input(f"Ingrese los minutos de ejercicio del día {dia + 1}: "))
    minutos_ejercicio.append(minutos)
    
    
    if minutos > 90:
        print("¡Felicidades! Has ejercitado más de 90 minutos hoy. Recuerda no exceder ese tiempo por motivos de salud.")


total_minutos = sum(minutos_ejercicio)


if total_minutos >= 150:
    print("¡Felicidades! Has alcanzado tu objetivo semanal de ejercicio.")
else:
    print("No has alcanzado el objetivo de 150 minutos. Te sugerimos incrementar tu actividad.")