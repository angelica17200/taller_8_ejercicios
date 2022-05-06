"""" Ejercicio 2
progrmam que permita realizar un prestamo bancario 
con ingresos superiores a $945200
y que no posea ninguna otra deuda"""

print("-------------------------------------")
print("---------VALOR DE INGRESO------------")
print("-------------------------------------")

#input
ingresos=int(input("Ingrese el valor de sus ingresos"))
deudas=int(input("Ponga 0 si no tiene deudas o si no digite 1 si tiene deudas "))

#processing 
if deudas==0  and ingresos>945200:
    print("Aprobado el prestamo")
elif deudas>0 and ingresos<945200:
        print("No puede ser aprobado")

