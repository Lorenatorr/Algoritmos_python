num_clientes= int(input("¿cuantos clientes desea registrar?"))
clientes=[]

for i in range (1, num_clientes + 1):
    encuesta=int(input(f" INGRESE SU CALIFICACION DE 1.0 A 5.0 {i}:"))
    clientes.append(encuesta)
    
    promedio= promedio + encuesta / num_clientes
