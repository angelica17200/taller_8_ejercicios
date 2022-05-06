"""" Ejercicio 1 
coordenadas cartesianas (p,y)"""

print("-------------------------------------")
print("-----Cuadrante plano cartesiano------")
print("-------------------------------------")

#input
x=int(input("Digite coordenadas x:"))
y=int(input("Digite coordenadas y:"))

#processing 
if x==0 and y==0:
    print("el punto esta sobre el eje x y el eje y")
elif x==0:
    print("el punto esta sobre el eje x")
elif y==0:
    print("el punto esta sobre el eje y:")

if x>0 and y>0:
    print("el punto pertenece al cuadrante I")
elif x<0 and y<o:
    print("el punto pertenece al cuadrante II")
elif x<0 and y<o:
    print("el punto pertenece al cuadrante III")
elif x>0 and y<0:
    print("el punto pertenece al cuadrante Iv")