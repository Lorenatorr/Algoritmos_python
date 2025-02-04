def verificar_turnos(empleados):
    resultados = []
    for i, empleado in enumerate(empleados):
        cumple = True
        for j in range(len(empleado) - 2):
            # Verifica si hay 3 días consecutivos con valor 1
            if empleado[j] == 1 and empleado[j + 1] == 1 and empleado[j + 2] == 1:
                cumple = False
                break
        resultados.append(cumple)
    return resultados

# Entrada de los turnos de los empleados
print("Ingrese los turnos de los empleados (7 días por empleado, use 1 para trabaja y 0 para no trabaja):")
empleados = []
for i in range(7):
    print(f"Empleado {i + 1}:")
    turnos = list(map(int, input("Ingrese los días (separados por espacios): ").split()))
    if len(turnos) != 7:
        print("Error: Debe ingresar exactamente 7 valores (1 o 0).")
        exit()
    empleados.append(turnos)

# Verificar las reglas
resultados = verificar_turnos(empleados)

# Imprimir los resultados
for i, cumple in enumerate(resultados):
    if cumple:
        print(f"Empleado {i + 1}: Cumple las reglas.")
    else:
        print(f"Empleado {i + 1}: No cumple las reglas (trabaja más de dos días consecutivos).")