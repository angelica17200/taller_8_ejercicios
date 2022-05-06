"""" Ejercicio 3
un programa que le indique el precio de venta
de un articulo dado El 15% si el costo es inferior a $3000.
 $500 si el costo está entre $3000 y $6000.
 El 25% si el costo supera los $6000"""

print("-------------------------------------")
print("-----PRECIO DE VENTA DEL ARTICULO ------")
print("-------------------------------------")

#input
precio_costo= float(input("Dame el precio del costo del articulo: "))

#processing 
if precio_costo<=3.000:
    ganancia= 0.15 * precio_costo
else:
    if precio_costo<=6.000:
        ganancia=500
    else:
            ganancia=precio_costo * 0.25
precio_venta = precio_costo + ganancia 

#output 
p=precio_costo+ganancia

print("El precio de venta del articulo de costo: " + str (precio_costo) + " es: " + str (p))


