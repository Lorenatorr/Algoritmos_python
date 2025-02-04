num_dias=int(input("¿cuántos dias de calorias desea registrar?"))
calorias=[]
for i in range (1, num_dias + 1):
    consumo=int(input(f"¿Ingrese el número de calorias del dia {i}:"))
    calorias.append(consumo)

    max_calorias = max(calorias)  
    min_calorias = min(calorias)  
    total_calorias=sum(calorias)/len(calorias)
    
    dia_max_ca = calorias.index(max_calorias) + 1  
    dia_min_ca = calorias.index(min_calorias) + 1

for i, calorias in enumerate(calorias):
    if calorias > 2500:
        calorias.append(i + 1)

if consumo:
    print("Advertencia: Los siguientes días se consumieron más de 2500 calorías:")
    for dia in calorias:
        print(f"  - Día {dia}")

if total_calorias > 2000:
    print("Advertencia: Ha superado la ingesta calórica recomendada de 2000 calorías diarias en promedio.")
else:
    print("Buen trabajo: Está dentro del rango calórico recomendado.")

            
print(f"El día con más consumo de calorias fue el día {dia_max_ca} con {max_calorias}")
print(f"El día con menos consumo de calorias fue el día {dia_min_ca} con {min_calorias}.")
print("el total de calorias consumidas es :", total_calorias)