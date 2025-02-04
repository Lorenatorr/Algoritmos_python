gastos_diarios = []

print("Ingrese sus gastos diarios durante 7 días:")
for i in range(7):
    gasto = float(input(f"Día {i + 1}: $"))
    gastos_diarios.append(gasto)


total_semanal = sum(gastos_diarios)


print("\n--- Análisis Diario ---")
for i, gasto in enumerate(gastos_diarios):
    if gasto > 20:
        print(f"Día {i + 1}: Gasto alto (${gasto:.2f})")


print("\n--- Resumen Semanal ---")
print(f"Total de gastos semanales: ${total_semanal:.2f}")

presupuesto_semanal = 100
if total_semanal > presupuesto_semanal:
    excedente = total_semanal - presupuesto_semanal
    print(f"Te has excedido del presupuesto por ${excedente:.2f}.")
else:
    restante = presupuesto_semanal - total_semanal
    print(f"Estás dentro del presupuesto. Te quedan ${restante:.2f}.")
