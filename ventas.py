num_dias=int(input("¿cuántos dias de ventas deseas registrar?"))
ventas=[]
for i in range (1, num_dias + 1):
    venta=int(input(f"¿Ingrese las ventas que obtuviste el día {i}:"))
    ventas.append(venta)

    max_ventas = max(ventas)  # Máximo de ventas
    min_ventas = min(ventas)  # Mínimo de ventas  
    total_ventas=sum(ventas)
    
    dia_max_ventas = ventas.index(max_ventas) + 1  # +1 porque los días empiezan desde 1
    dia_min_ventas = ventas.index(min_ventas) + 1
    
    print("el total de las ventas es :", total_ventas)
    print(f"El día con más ventas fue el día {dia_max_ventas} con {max_ventas} ventas.")
    print(f"El día con menos ventas fue el día {dia_min_ventas} con {min_ventas} ventas.")
