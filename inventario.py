stock =[]

print("Por favor ingrese las cantidades en stock para los tipos de camiseta:")

for i in range (1,11):
    cantidad=int(input(f"Cantidad del tipo de camiseta {i}: "))
    stock.append(cantidad)
    
    total_camisetas=sum(stock)
    print ("la cantidad de camisetas del inventario  es :", total_camisetas)
 
 