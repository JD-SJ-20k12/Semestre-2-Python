#Juan De Dios Sanchez Juarez 
#2079270

#Inicio del programa (se guardan todas las variables)
distancia_km=80
dinero=500

#Pedimos la informacion al usuario
print("¿Cual es el rendimiento? ")
rendimiento=float(input())
if rendimiento>0:
    print("¿Cual es el costo por litro de gasolina?")
    costo_gasolina=float(input())
else:
    print("Ha ocurrido un error, por favor intente revisar el dato que puso")

#Se calculan los datos finales
gasolina=dinero/costo_gasolina
intervalo=gasolina*rendimiento
tiempo_decimal=intervalo/distancia_km
tiempo_hora_entero=int(tiempo_decimal)
tiempo_minutos_entero=(60*(tiempo_decimal-tiempo_hora_entero))

#Fin del programa
print("--------\nCon $",dinero,"pesos")
print("se recorre:",distancia_km,"km")
print("En: ",tiempo_hora_entero,"Horas",tiempo_minutos_entero,"minutos")